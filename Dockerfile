FROM python:3.9-slim

# Cria o diretório da aplicação
WORKDIR /app

# Cria o arquivo app.py
RUN echo 'from flask import Flask, request, jsonify\n\
import subprocess\n\
\n\
app = Flask(__name__)\n\
\n\
@app.route("/convert", methods=["POST"])\n\
def convert_pdf_to_json():\n\
    if "file" not in request.files:\n\
        return jsonify({"error": "No file part"}), 400\n\
    \n\
    file = request.files["file"]\n\
    file_path = f"/app/{file.filename}"\n\
    file.save(file_path)\n\
    \n\
    try:\n\
        result = subprocess.run(["python", "/app/pdf_to_json.py", file_path], capture_output=True, text=True)\n\
        if result.returncode != 0:\n\
            return jsonify({"error": result.stderr}), 500\n\
        \n\
        return jsonify({"json": result.stdout})\n\
    except Exception as e:\n\
        return jsonify({"error": str(e)}), 500\n\
\n\
if __name__ == "__main__":\n\
    app.run(host="0.0.0.0")' > /app/app.py

# Cria o arquivo pdf_to_json.py
RUN echo 'import pdfplumber\n\
import json\n\
import sys\n\
\n\
def pdf_to_json(pdf_path):\n\
    with pdfplumber.open(pdf_path) as pdf:\n\
        pages = [page.extract_text() for page in pdf.pages]\n\
    return json.dumps(pages, ensure_ascii=False)\n\
\n\
if __name__ == "__main__":\n\
    if len(sys.argv) != 2:\n\
        print("Usage: python pdf_to_json.py <pdf_path>")\n\
        sys.exit(1)\n\
    \n\
    pdf_path = sys.argv[1]\n\
    print(pdf_to_json(pdf_path))' > /app/pdf_to_json.py

# Instala as dependências
RUN pip install flask pdfplumber

# Expõe a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
