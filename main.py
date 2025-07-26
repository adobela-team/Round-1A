import fitz  # PyMuPDF
import os
import json

def extract_title(page): 
    title = ""
    max_size = 0
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if s["size"] > max_size and s["text"].strip(): 
                    max_size = s["size"]
                    title = s["text"].strip()
    return title

def extract_headings(doc):
    font_sizes = set()
    spans = []
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    size = round(s["size"], 1)
                    text = s["text"].strip()
                    if not text:
                        continue
                    if len(text.split()) > 15:
                        continue
                    is_bold = (s.get("flags", 0) & 2) != 0
                    font_sizes.add(size)
                    spans.append({
                        "size": size,
                        "text": text,
                        "page": page_num,
                        "bold": is_bold
                    })
    size_levels = sorted(font_sizes, reverse=True)[:3]
    level_map = {size: f"H{idx+1}" for idx, size in enumerate(size_levels)}

    min_size_for_heading = size_levels[-1] if size_levels else 0

    headings = []
    for span in spans:
        size = span["size"]
        text = span["text"]
        page_num = span["page"]
        bold = span["bold"]

        
        if not text or text == '""' or text == "''" or text.strip('\u200b') == '' or len(text) == 1:
            continue

        if size in level_map:
            level = level_map[size]
            headings.append({"level": level, "text": text, "page": page_num})
        elif bold and size >= (min_size_for_heading * 0.85):
            headings.append({"level": "H3", "text": text, "page": page_num})

    level_order = {"H1": 1, "H2": 2, "H3": 3}
    headings = sorted(headings, key=lambda h: (level_order.get(h["level"], 99), h["page"]))
    return headings

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = extract_title(doc[0]) if len(doc) > 0 else ""
    headings = extract_headings(doc)
    return {"title": title, "outline": headings}

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in the '{input_dir}' directory. Please add PDFs and rerun.")
        return
    for filename in pdf_files:
        pdf_path = os.path.join(input_dir, filename)
        print(f"Processing file: {filename}")
        try:
            result = process_pdf(pdf_path)
            json_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"Saved JSON to: {json_path}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    main()