import pdfplumber
import json
import sys

def pdf_to_json(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    return json.dumps(pages, ensure_ascii=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_json.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    print(pdf_to_json(pdf_path))
