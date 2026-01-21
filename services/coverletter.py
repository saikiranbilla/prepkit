import os
import torch
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from utils.prompt_templates import COVER_LETTER_PROMPT

app = Flask(__name__)

# CONFIGURATION
MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
# Use 4-bit quantization to run on consumer hardware (8GB RAM requirement)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

print(f"Loading {MODEL_ID} with 4-bit quantization...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto"
)

# Initialize RAG Embeddings (retrieves relevant skills/experiences)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def retrieve_relevant_context(resume_text, job_description):
    """
    Splits resume into chunks and retrieves the parts most relevant 
    to the job description using vector similarity.
    """
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(resume_text)
    
    # Create vector store from resume chunks
    vectorstore = FAISS.from_texts(chunks, embeddings)
    
    # Find top 3 chunks matching the job description
    docs = vectorstore.similarity_search(job_description, k=3)
    return "\n".join([d.page_content for d in docs])

@app.route('/generate', methods=['POST'])
def generate_cover_letter():
    data = request.json
    resume_text = data.get('resume_text')
    job_description = data.get('job_description')

    if not resume_text or not job_description:
        return jsonify({"error": "Missing resume or job description"}), 400

    try:
        # Step 1: RAG - Get most relevant resume sections
        relevant_context = retrieve_relevant_context(resume_text, job_description)

        # Step 2: Construct the Prompt
        # We instruct LLaMA to be professional, concise, and use the retrieved context
        prompt = COVER_LETTER_PROMPT.format(
            context=relevant_context,
            job_desc=job_description
        )

        messages = [
            {"role": "system", "content": "You are an expert career coach. Write a compelling, personalized cover letter."},
            {"role": "user", "content": prompt}
        ]

        # Step 3: Inference
        input_ids = tokenizer.apply_chat_template(
            messages, 
            add_generation_prompt=True, 
            return_tensors="pt"
        ).to(model.device)

        terminators = [
            tokenizer.eos_token_id,
            tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = model.generate(
            input_ids,
            max_new_tokens=800,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
        )

        response = outputs[0][input_ids.shape[-1]:]
        cover_letter = tokenizer.decode(response, skip_special_tokens=True)

        return jsonify({
            "status": "success",
            "cover_letter": cover_letter,
            "used_context": relevant_context  # Useful for debugging RAG
        })

    except Exception as e:
        print(f"Inference Error: {str(e)}")
        return jsonify({"error": "Failed to generate cover letter"}), 500

if __name__ == '__main__':
    # Run on port 5002 as defined in Architecture
    app.run(host='0.0.0.0', port=5002)
