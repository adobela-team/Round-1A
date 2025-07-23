# PDF Outline Extractor

## 🚀 Project Overview
The PDF Outline Extractor is a robust and efficient tool designed to extract structured outlines from PDF documents. It intelligently identifies and extracts the document's Title along with hierarchical headings (H1, H2, H3), providing a clean and organized JSON representation of the content structure. This tool is ideal for developers, researchers, and professionals who need to analyze or repurpose PDF content programmatically.

## ✨ Key Features 
- Accurate extraction of Titles and multi-level headings based on font size and style heuristics.
- Supports extraction of headings up to three levels deep (H1, H2, H3).
- Outputs results in a well-structured JSON format for easy integration with other tools or workflows.
- Lightweight and fast, processing documents within seconds without relying on external models.
- Fully offline and CPU-only operation, ensuring privacy and compatibility with AMD64 architectures.
- Dockerized for seamless deployment and consistent runtime environments.

## 🧠 Technology Stack & Approach
- Built using Python and PyMuPDF (fitz) for precise PDF text extraction.
- Utilizes font size and boldness heuristics to determine heading levels, mimicking human reading patterns.
- Extracts the largest font on the first page as the document Title.
- Implements filtering to exclude irrelevant or malformed headings, ensuring clean output.
- Designed with performance and resource constraints in mind, suitable for integration into larger pipelines.

## 📦 Installation & Usage

### Build the Docker Image
```bash
docker build --platform linux/amd64 -t outlineextractor:abc123 .
```

### Run the Extractor
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outlineextractor:abc123
```

- Place your PDF files in the `input` directory.
- Extracted JSON outlines will be saved in the `output` directory with corresponding filenames.

## ⚙️ Performance & Constraints
- Entirely offline, no internet connection required.
- CPU-only execution optimized for AMD64 platforms.
- Minimal resource footprint with model size under 200MB (no external models).
- Processes typical PDF documents within 10 seconds, suitable for batch processing.

## 💡 Use Cases
- Automating document summarization and indexing.
- Enhancing search and navigation in large PDF repositories.
- Preparing content for web publishing or eBook generation.
- Assisting in academic research by extracting structured outlines.
- Integrating with content management systems for metadata extraction.




