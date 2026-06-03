# 🎓 EduMind AI

### Intelligent Educational Chatbot using RAG, FastAPI & LLMs

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green.svg">
  <img src="https://img.shields.io/badge/RAG-AI-orange.svg">
  <img src="https://img.shields.io/badge/LLM-Powered-purple.svg">
  <img src="https://img.shields.io/badge/Status-Active-success.svg">
</p>

---

## 🚀 Overview

EduMind AI is an AI-powered educational assistant that leverages Retrieval-Augmented Generation (RAG) to deliver accurate, context-aware answers across STEM subjects.

Instead of relying solely on Large Language Models, EduMind AI retrieves relevant knowledge from a custom knowledge base using semantic search and vector embeddings before generating responses.

This significantly improves answer quality while reducing hallucinations.

---

## ✨ Features

✅ AI-Powered Educational Chatbot

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search using Vector Embeddings

✅ FastAPI Backend

✅ Context-Aware Question Answering

✅ STEM Subject Support

✅ User Authentication System

✅ Modular AI Architecture

✅ Fast Response Generation

✅ Scalable Knowledge Base Integration

---

## 🧠 Architecture

User Question
↓
Embedding Generation
↓
Semantic Search
↓
Top Relevant Chunks Retrieval
↓
Context Injection
↓
LLM Response Generation
↓
Final Answer

---

## ⚙️ Tech Stack

| Component  | Technology                     |
| ---------- | ------------------------------ |
| Backend    | FastAPI                        |
| Language   | Python                         |
| Embeddings | BAAI/bge-small-en-v1.5         |
| NLP        | Sentence Transformers          |
| Retrieval  | Cosine Similarity              |
| Templates  | Jinja2                         |
| Storage    | Pickle Vector Store            |
| AI Layer   | Retrieval-Augmented Generation |

---

## 📂 Project Structure

```bash
EduMind-AI/
│
├── app.py
├── model.py
├── chunks.pkl
├── embeddings.pkl
│
├── rag/
│   ├── load_embeddings.py
│   ├── retriever.py
│   └── generator.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── chatbot.html
│   └── about.html
│
└── vector_db/
```

## 🔍 How It Works

### Step 1

User submits a question.

### Step 2

Question is converted into vector embeddings.

### Step 3

Semantic similarity search finds relevant knowledge chunks.

### Step 4

Top matching contexts are retrieved.

### Step 5

Retrieved knowledge is passed to the LLM.

### Step 6

AI generates a contextual and accurate answer.

---

## 🎯 Example

### User Question

```text
Explain Newton's First Law of Motion
```

### AI Response

```text
Newton's First Law states that an object remains at rest or in uniform motion unless acted upon by an external force.
```

---

## 📈 Future Enhancements

* Vector Database Integration (FAISS / ChromaDB)
* Advanced RAG Pipelines
* Multi-Document Retrieval
* Hybrid Search
* User Memory
* Voice Assistant Support
* LLM Fine-Tuning
* Multi-Language Support

---

## 💡 Learning Outcomes

This project demonstrates practical implementation of:

* Generative AI
* Retrieval-Augmented Generation
* Semantic Search
* Vector Embeddings
* FastAPI Development
* NLP Applications
* AI System Design
* Production AI Workflows

---

## 🏆 Project Highlights

✔ Reduced LLM Hallucinations

✔ Context-Aware Responses

✔ Fast Retrieval Mechanism

✔ Modular Architecture

✔ Real-World AI Application

✔ Industry-Relevant AI Skills

---

## 👨‍💻 Author

### Chandru

AI Engineer | Machine Learning Engineer | Generative AI Developer

Passionate about building intelligent systems using LLMs, RAG, Computer Vision, NLP, and Production AI Architectures.

---

⭐ If you found this project useful, consider giving it a star!
