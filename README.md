# PDF Intelligence Engine

A Retrieval-Augmented Generation (RAG) application built using Streamlit, ChromaDB, LangChain, and HuggingFace Embeddings.

## 🚀 Live Demo

Streamlit App:

https://ai-engineering-day2-pdf-intelligence-engine-erhpg6f2azzxopaxyd.streamlit.app/

---

## Project Overview

PDF Intelligence Engine allows users to upload PDF documents and ask questions about their contents. The application uses semantic search and vector embeddings to retrieve the most relevant information from uploaded PDFs.

This project demonstrates the core concepts behind modern AI-powered document question-answering systems.

---

## Features

* Upload PDF documents
* Automatic text extraction
* Text chunking using LangChain
* Vector embeddings using HuggingFace Sentence Transformers
* ChromaDB vector storage
* Semantic search and retrieval
* Streamlit web interface
* Source chunk display for retrieved answers
* Cloud deployment using Streamlit Community Cloud

---

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* PyPDF
* Sentence Transformers

---

## Architecture

```text
PDF Upload
     │
     ▼
Text Extraction
     │
     ▼
Chunking
     │
     ▼
Embeddings
     │
     ▼
ChromaDB
     │
     ▼
Semantic Search
     │
     ▼
Relevant Chunks
     │
     ▼
Answer Display
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Chandana1707/ai-engineering-day2-pdf-intelligence-engine.git

cd ai-engineering-day2-pdf-intelligence-engine
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

---

## Usage

1. Upload a PDF document.
2. Wait for processing and embedding creation.
3. Enter a question related to the document.
4. View the retrieved relevant content.

---

## Learning Outcomes

* Vector Databases
* Embeddings
* Semantic Search
* ChromaDB
* LangChain
* Retrieval-Augmented Generation (RAG)
* Streamlit Deployment
* AI Application Development

---

## Future Improvements

* Groq/OpenAI integration
* Chat-based conversational memory
* Source page citations
* Multi-PDF support
* User authentication
* Docker deployment
* Production-grade RAG pipeline

---

## Author

**Chandana**

B.Tech CSE Student

AI Engineering Learning Journey – Day 2 Capstone Project

---

## Project Status

✅ Day 2 Capstone Completed

✅ GitHub Repository Published

✅ Streamlit Deployment Successful
