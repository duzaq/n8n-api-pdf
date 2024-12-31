FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
