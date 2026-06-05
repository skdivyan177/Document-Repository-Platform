# Document Repository Platform

This project is a Flask-based document repository that supports file uploads, PDF metadata extraction, document search, along with file retrieval. Metadata is automatically stored in a SQLite database, the categories being filename, page count, file size, and upload date.

## Technologies

- Python
- Flask
- SQLite
- PyPDF
- Docker
- Git

## Features

- Upload documents
- Extract PDF metadata
- Store metadata in SQLite
- Search documents by filename
- Download stored documents

## Run
Commands:
```bash
pip install flask pypdf
python app.py
```
Application runs on: http://localhost:5000

## Documentation

- docs/architecture.md
- docs/troubleshooting.md
- docs/architecture.png
