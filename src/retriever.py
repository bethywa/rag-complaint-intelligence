from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def retrieve_chunks(index, store_data, question, k=5):
    query_vec = model.encode([question]).astype("float32")
    distances, indices = index.search(query_vec, k)

    results = []
    for idx in indices[0]:
        results.append({
            "text": store_data["documents"][idx],
            "metadata": store_data["metadata"][idx]
        })

    return results
