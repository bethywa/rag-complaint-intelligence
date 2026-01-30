import faiss
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FAISS_DIR = BASE_DIR / "vector_store" / "faiss"

def load_faiss_store():
    index = faiss.read_index(str(FAISS_DIR / "index.faiss"))
    with open(FAISS_DIR / "metadata.pkl", "rb") as f:
        data = pickle.load(f)
    return index, data
