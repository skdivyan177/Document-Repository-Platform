from flask import Flask, request
from database import init_db, insert_document, get_all_documents
import os

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

    insert_document(file.filename, file_size)
    
    return {
        "message": "uploaded successfully",
        "filename": file.filename
    }

@app.route("/documents")
def documents(): 
    documents = get_all_documents()
    return {
        "documents" : documents
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)