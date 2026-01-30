# 📊 Complaint Intelligence RAG System

A production-ready **Retrieval-Augmented Generation (RAG)** system for analyzing and answering questions about **financial consumer complaints**.  
This project is built as part of the **10 Academy Week 7 Challenge**, focusing on end-to-end data processing, semantic search, and LLM-based question answering.

The system enables analysts to explore complaint narratives, identify patterns, and generate **context-aware answers** using vector embeddings and a Large Language Model (LLM).

---

## 🚀 Project Overview

**Business Context:**  
CrediTrust is a financial services company that receives thousands of customer complaints.  
Manually analyzing these complaints is slow and inefficient.

**Solution:**  
This project builds a **Complaint Intelligence Assistant** that:
- Understands natural language questions
- Retrieves relevant complaint records
- Generates accurate, grounded answers using an LLM

---

## ✨ Key Features

- 📂 End-to-end complaint data pipeline
- 🔍 Semantic search using FAISS vector index
- 🧠 Retrieval-Augmented Generation (RAG)
- 📊 Exploratory Data Analysis (EDA)
- 🧪 Evaluation of answer quality
- 🖥️ Interactive web application (Streamlit UI)
- ♻️ Modular, production-style codebase

---

## 🧠 System Architecture

# 📊 Complaint Intelligence RAG System

A production-ready **Retrieval-Augmented Generation (RAG)** system for analyzing and answering questions about **financial consumer complaints**.  
This project is built as part of the **10 Academy Week 7 Challenge**, focusing on end-to-end data processing, semantic search, and LLM-based question answering.

The system enables analysts to explore complaint narratives, identify patterns, and generate **context-aware answers** using vector embeddings and a Large Language Model (LLM).

---

## 🚀 Project Overview

**Business Context:**  
CrediTrust is a financial services company that receives thousands of customer complaints.  
Manually analyzing these complaints is slow and inefficient.

**Solution:**  
This project builds a **Complaint Intelligence Assistant** that:
- Understands natural language questions
- Retrieves relevant complaint records
- Generates accurate, grounded answers using an LLM

---

## ✨ Key Features

- 📂 End-to-end complaint data pipeline
- 🔍 Semantic search using FAISS vector index
- 🧠 Retrieval-Augmented Generation (RAG)
- 📊 Exploratory Data Analysis (EDA)
- 🧪 Evaluation of answer quality
- 🖥️ Interactive web application (Streamlit UI)
- ♻️ Modular, production-style codebase

---

## 🧠 System Architecture

   ┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         ▼
┌──────────────────────────┐
│      RAG Pipeline        │
│                          │
│  ┌───────────────┐       │
│  │   Retriever   │───────┼──► FAISS Vector Store
│  │ (MiniLM Emb.) │       │
│  └───────────────┘       │
│                          │
│  ┌───────────────┐       │
│  │   Generator   │───────┼──► LLM (FLAN-T5)
│  └───────────────┘       │
└────────┬─────────────────┘
         │
         ▼
┌─────────────────┐
│  Answer +       │
│  Source Chunks  │
└─────────────────┘





---

## 🛠️ Core Technologies

- **Python 3.9+**
- **Pandas, NumPy** – data processing
- **Sentence-Transformers** – embeddings
- **FAISS** – vector similarity search
- **Hugging Face Transformers** – LLM
- **Gardio** – web UI
- **Jupyter Notebooks** – experimentation & evaluation

---

## 📁 Project Structure

rag-complaint-intelligence/
├── .github/workflows/
│ └── unittests.yml
├── data/
│ ├── raw/
│ │ └── complaints.csv
│ └── processed/
│ ├── filtered_complaints.csv
│ └── sampled_complaints.csv
├── notebooks/
│ ├── task1_eda.ipynb
│ ├── task2_chunking_embedding_indexing.ipynb
│ └── task3_evaluation.ipynb
├── src/
│ ├── preprocessing.py
│ ├── build_faiss_index.py
│ ├── vector_store.py
│ ├── retriever.py
│ ├── generator.py
│ ├── prompt.py
│ └── pipeline.py
├── vector_store/
│ └── faiss/
│ ├── index.faiss
│ └── metadata.pkl
├── app.py
├── requirements.txt
├── README.md
└── .gitignore




---

## 📌 Tasks Overview

### ✅ Task 1: Exploratory Data Analysis & Preprocessing
**Objective:** Understand the dataset and prepare high-quality complaint narratives.

**Key Activities:**
- Load and inspect raw complaint data
- Analyze complaint distribution and text length
- Filter invalid or missing narratives
- Clean and normalize text

**Deliverables:**
- ✅ Cleaned and filtered dataset
- ✅ EDA visualizations
- ✅ `filtered_complaints.csv`

**Notebook:**  
`notebooks/task1_eda.ipynb`

---

### ✅ Task 2: Chunking, Embedding & Vector Indexing
**Objective:** Convert complaint narratives into searchable vector representations.

**Key Components:**
- Text chunking strategy
- Sentence embeddings using `all-MiniLM-L6-v2`
- FAISS index creation and persistence

**Deliverables:**
- ✅ Complaint embeddings
- ✅ FAISS vector index
- ✅ Metadata storage

**Notebook:**  
`notebooks/task2_chunking_embedding_indexing.ipynb`

---

### ✅ Task 3: RAG Pipeline Implementation & Evaluation
**Objective:** Build and evaluate the full RAG pipeline.

**Key Components:**
- **Retriever:** Semantic similarity search (top-k retrieval)
- **Prompt Engineering:** Analyst-focused, context-only answers
- **Generator:** LLM-based response generation
- **Evaluation:** Qualitative assessment with representative queries

**Modules:**
- `src/retriever.py`
- `src/prompt.py`
- `src/generator.py`
- `src/pipeline.py`

**Deliverables:**
- ✅ End-to-end RAG pipeline
- ✅ Evaluation results
- ✅ Quality analysis

**Notebook:**  
`notebooks/task3_evaluation.ipynb`

---

### ✅ Task 4: Application Development
**Objective:** Provide an interactive interface for users.

**Features:**
- Chat-style UI
- Fixed input and action buttons
- Context-aware responses
- Clear and professional UX

**Entry Point:**  
`app.py`

---

## ▶️ Installation & Running the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/rag-complaint-intelligence.git
cd rag-complaint-intelligence


## 2️⃣ Create Virtual Environment
  python -m venv .venv
  source .venv/Scripts/activate   # Windows

 ## 3️⃣ Install Dependencies
      pip install -r requirements.txt

## 4️⃣ Run the Application
    Gardio run app.py


####📊 Project Status
✅ Completed

  . Data preprocessing & EDA
  . Embedding & FAISS indexing
  . RAG pipeline
  . Evaluation framework
  . gardio application

### 🚧 Planned Improvements

 . Performance optimization
 . Docker deployment
 . REST API
 . Advanced analytics dashboard

#### 📝 Notes

This project is part of an educational portfolio and demonstrates best practices in:

 . Data Engineering
 . Machine Learning
 . NLP
 . LLM-based systems

👤 Author

Bethelihem


