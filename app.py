import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

st.title("📄 PDF Intelligence Engine")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded")

    loader = PyPDFLoader(path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(
        documents
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="chroma_db"
    )

    query = st.text_input(
        "Ask a question"
    )

    if query:

        results = db.similarity_search(
            query,
            k=3
        )

        st.subheader("Relevant Chunks")

        for doc in results:
            st.write(doc.page_content)