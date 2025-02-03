from llama_cpp import Llama

def load_llama_model(model_path):
    """Upload Llama model"""
    return Llama(
        model_path=model_path,
        n_threads=8,
        n_ctx=2048,
        temperature=0.7,
        top_p=0.9,
        max_tokens=200
    )

def generate_response(llm, user_input):
    """Model answer"""
    response = llm.create_chat_completion(messages=[
        {"role": "system", "content": "You are an AI cocktail expert."},
        {"role": "user", "content": user_input}
    ], max_tokens=300)

    return response["choices"][0]["text"].strip()