from src.vector_store import load_faiss_store
from src.retriever import retrieve_chunks
from src.prompt import build_prompt
from src.generator import generate_answer


MAX_CONTEXT_CHARS = 1800  # safe limit for T5-style models


def run_pipeline(question, k=5):
    # Load FAISS index + metadata
    index, store_data = load_faiss_store()

    # Retrieve top-k chunks
    retrieved = retrieve_chunks(index, store_data, question, k)

    # Build context safely (prevent token overflow)
    context_parts = []
    current_length = 0

    for r in retrieved:
        text = r["text"]
        if current_length + len(text) > MAX_CONTEXT_CHARS:
            break
        context_parts.append(text)
        current_length += len(text)

    context = "\n\n---\n\n".join(
    f"Company: {r['metadata'].get('company', 'Unknown')}\nComplaint: {r['text']}"
    for r in retrieved
    )


    # Build prompt
    prompt = build_prompt(context, question)

    # Generate answer
    answer = generate_answer(prompt)

    return answer, retrieved


if __name__ == "__main__":
    question = "What are common complaints related to billing errors on credit cards?"
    answer, sources = run_pipeline(question)

    print("\nANSWER:\n", answer)
    print("\nSOURCES:\n", sources[:2])
