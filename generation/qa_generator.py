from transformers import pipeline

def generate_answer(query, context):
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    generator = pipeline("text-generation", model="gpt2")
    result = generator(prompt, max_length=200, do_sample=True, temperature=0.7)[0]["generated_text"]
    return result
