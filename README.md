# PDF Outline Extractor

## 🚀 Overview
Extracts Title, H1, H2, H3 headings from PDFs and exports as JSON in a clean hierarchy.

## 🧠 Approach
- Used PyMuPDF to read text spans with font size and position
- Heuristics based on font size and style for heading levels
- Extracted largest font from Page 1 as Title

## 📦 How to Build & Run

Build:
```bash
docker build --platform linux/amd64 -t outlineextractor:abc123 .
```

Run:
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outlineextractor:abc123
```

## ✅ Constraints Met

* Offline-only
* CPU-only (AMD64)
* Model size ≤ 200MB (no external models used)
* Runs within 10 seconds
