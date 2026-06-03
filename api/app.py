from flask import Flask, request
from database import (init_db, insert_document, 
                      get_all_documents, search_documents)
import os
from pypdf import PdfReader
from flask import send_from_directory

app = Flask(__name__)
init_db()

@app.route("/")
def health():
    return {
        "status": "running",
        "service": "document repository platform"
    }

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    save_path = os.path.join("uploads", file.filename)

    file.save(save_path)
    file_size = os.path.getsize(save_path)
    page_count = 0

    if file.filename.lower().endswith(".pdf"):
        reader = PdfReader(save_path)
        page_count = len(reader.pages)
    
    insert_document(file.filename, page_count, file_size) 
    return {
        "message": "uploaded successfully",
        "filename": file.filename,
        "page_count": page_count,
        "file_size": file_size
    }

@app.route("/documents")
def documents(): 
    documents = get_all_documents()
    return {
        "documents" : documents
    }

@app.route("/search")
def search():
    search_term = request.args.get("filename", "")
    documents = search_documents(search_term)
    return {
        "documents": documents
    }

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(""
    "uploads",
    filename, 
    as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
