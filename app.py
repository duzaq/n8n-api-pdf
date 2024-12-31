from flask import Flask, request, jsonify
import subprocess
import json  # Importe o módulo json aqui

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_json():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    file_path = f"/app/{file.filename}"
    file.save(file_path)
    
    try:
        result = subprocess.run(["python", "/app/pdf_to_json.py", file_path], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500
        
        return jsonify({"json": json.loads(result.stdout)})  # Agora você pode usar json.loads()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
