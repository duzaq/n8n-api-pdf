import camelot
import json
import sys

def pdf_table_to_json(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all')
    table_data = [table.df.to_dict(orient='records') for table in tables]
    return json.dumps(table_data, ensure_ascii=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python pdf_table_to_json.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    print(pdf_table_to_json(pdf_path))
