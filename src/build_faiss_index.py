import faiss
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PARQUET = BASE_DIR / "vector_store" / "complaint_embeddings.parquet"
FAISS_DIR = BASE_DIR / "vector_store" / "faiss"
FAISS_DIR.mkdir(exist_ok=True)

print("📦 Loading embeddings...")
df = pd.read_parquet(PARQUET, columns=["embedding", "document", "metadata"])

embeddings = np.vstack(df["embedding"].values).astype("float32")

print("🔧 Building FAISS index...")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, str(FAISS_DIR / "index.faiss"))

with open(FAISS_DIR / "metadata.pkl", "wb") as f:
    pickle.dump(
        {
            "documents": df["document"].tolist(),
            "metadata": df["metadata"].tolist()
        },
        f
    )

print("🎉 FAISS indexing complete!")
print("📊 Total vectors:", index.ntotal)
