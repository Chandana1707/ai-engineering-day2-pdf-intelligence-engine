# PDF Intelligence Engine

A Retrieval-Augmented Generation (RAG) application built using Streamlit, ChromaDB, LangChain, and HuggingFace Embeddings.

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

## Project Structure

```text
pdf-intelligence-engine/
│
├── app.py
├── uploads/
├── chroma_db/
├── logs/
├── requirements.txt
├── .gitignore
└── README.md
```

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

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

## Usage

1. Launch the application.
2. Upload a PDF file.
3. Wait for document processing.
4. Enter a question related to the PDF.
5. View the most relevant retrieved content.

---

## Example Questions

* What is Python?
* Explain normalization.
* What is operating system scheduling?
* What are the advantages of FastAPI?
* What is Retrieval-Augmented Generation?

---

## Learning Outcomes

This project helped demonstrate:

* Vector databases
* Embeddings
* Semantic search
* Document chunking
* Retrieval-Augmented Generation (RAG)
* Streamlit application development
* LangChain integration

---

## Future Improvements

* Groq/OpenAI LLM integration
* Chat history support
* Source page citations
* Multi-PDF support
* User authentication
* Docker deployment
* Cloud deployment

---

## Author

**Chandana**

B.Tech CSE Student
AI Engineering Learning Journey – Day 2 Capstone Project

---
