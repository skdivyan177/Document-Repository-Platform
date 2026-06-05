# Architecture Overview
This Document Repository Platform consists of three primary components:

## #1 Flask API
Provided endpoints for document upload, search, retrieval, and download.

## #2 Repository Storage
Uploaded files are stored in the uploads directory.

## #3 Metadata Database
Document metadata is stored in SQLite, the metadata inclues:
- Filename
- Page Count
- File Size
- Upload Date

## Metadata Pipeline
Upload Document
→ Extract Metadata
→ Store Metadata
→ Search/Retrieve