from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1
)

def generate_answer(prompt):
    output = generator(prompt, max_new_tokens=256, do_sample=False)
    return output[0]["generated_text"]
