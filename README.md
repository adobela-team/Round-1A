# PDF Outline Extractor

##  Project Overview
The PDF Outline Extractor is a smart and efficient tool designed to extract structured outlines from PDF documents. It intelligently identifies and extracts the document's Title along with hierarchical headings (H1, H2, H3), providing a clean and organized JSON representation of the content structure. This tool is ideal for developers, researchers, and professionals who need to analyze or repurpose PDF content programmatically.

##  Key Features 
- Accurate extraction of Titles and multi-level headings based on font size, boldness and style heuristics. 
- Supports extraction of headings up to three levels deep (H1, H2, H3).
- Outputs results in a well-structured JSON format for easy integration with other tools or workflows. 
-  Also extracts headings from multilingual languages (hindi and japanese). 
- Lightweight and fast, processing documents within seconds without relying on external models.
- Fully offline and CPU-only operation, ensuring privacy and compatibility with AMD64 architectures.
- Dockerized for seamless deployment and consistent runtime environments.

##  Technology Stack & Approach
- Built using Python and PyMuPDF (fitz) for precise PDF text extraction.
- Utilizes font size and boldness heuristics to determine heading levels, mimicking human reading patterns.
- Extracts the largest font on the first page as the document Title.
- Implements filtering to exclude irrelevant or malformed headings, ensuring clean output.
- Designed with performance and resource constraints in mind, suitable for integration into larger pipelines.

##  Project Directory Structure 

```
📁 Round 1A 
│
├── 📁 input/
│   ├── .gitkeep
│   ├── English.01.pdf
│   ├── English.02.pdf
│   ├── English.03.pdf
│   ├── English.04.pdf
│   └── Hindi.pdf
│
├── 📁 output/
│   ├── .gitkeep
│   ├── English.01.json
│   ├── English.02.json
│   ├── English.03.json
│   ├── English.04.json
│   └── Hindi.json
│
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
└── schema.json 

```
##  Installation & Usage

### Build the Docker Image
```bash
docker build --platform linux/amd64 -t outlineextractor:abc123 .
```

### Run the Extractor
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outlineextractor:abc123
```

- PDF files are in the `input` directory. 
- Extracted JSON outlines will be saved in the `output` directory with corresponding filenames.

##  Performance & Constraints
- Entirely offline, no internet connection required.
- CPU-only execution optimized for AMD64 platforms.
- Minimal resource footprint with model size under 200MB (no external models).
- Processes typical PDF documents within 10 seconds.

##  Use Cases
 - Automated Document Outlining

- Detects and extracts headings (H1, H2, H3) based on font size and boldness.
- Creates a clean outline structure that mirrors the original document’s hierarchy.  

 - Dynamic Title Extraction

- Identifies the most prominent text (by font size) on the first page as the document’s title.

 - Bulk PDF Processing

- Scans multiple PDF files from the input/ folder.
- Outputs structured .json summaries into output/, ready for integration.

 - Integration with Content Systems

- Extracted JSON structure can be consumed by:
    - Web apps for displaying content
    - AI chatbots for answering queries based on documents
    - Content Management Systems (CMS) for automated categorization  


##  Show Your Support
- If this project aligned with your interests or provided useful insights, feel free to:
     - Star the repository
     - Fork it to explore or enhance it furtherFork it to explore or enhance it further
     - We were happy to connect! Reach us at: codec.connect@gmail.com 

- We were grateful for your time and interest — Thank you for reviewing our submission.            
