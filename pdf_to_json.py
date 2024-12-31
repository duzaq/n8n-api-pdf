import camelot
import json
import sys

def pdf_table_to_json(pdf_path):
    # Extrair tabelas do PDF
    tables = camelot.read_pdf(pdf_path, pages='all')
    
    # Listas para armazenar entradas e saídas
    entradas = []
    saidas = []
    
    # Processar cada tabela
    for table in tables:
        # Converter a tabela para um DataFrame do Pandas
        df = table.df
        
        # Ignorar o cabeçalho (primeira linha) e processar as transações
        for i in range(1, len(df)):  # Começa da segunda linha (índice 1)
            # Criar o dicionário no formato desejado
            transacao = {
                "DESCRIÇÃO": df.iloc[i, 0],  # Acessa a primeira coluna
                "DATA": df.iloc[i, 1],       # Acessa a segunda coluna
                "HORA": df.iloc[i, 2],       # Acessa a terceira coluna
                "VALOR": df.iloc[i, 3],      # Acessa a quarta coluna
                "SALDO": df.iloc[i, 4],      # Acessa a quinta coluna
                "CARTÃO": df.iloc[i, 5]      # Acessa a sexta coluna
            }
            
            # Verificar se é uma entrada ou saída
            if "-" in transacao["VALOR"]:
                saidas.append(transacao)  # Adicionar à lista de saídas
            else:
                entradas.append(transacao)  # Adicionar à lista de entradas
    
    # Retornar as listas de entradas e saídas em formato JSON
    return json.dumps({"entradas": entradas, "saidas": saidas}, ensure_ascii=False)

if __name__ == '__main__':
    # Verificar se o caminho do PDF foi passado como argumento
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_json.py <pdf_path>")
        sys.exit(1)
    
    # Caminho do PDF passado como argumento
    pdf_path = sys.argv[1]
    
    # Converter o PDF para JSON e imprimir o resultado
    print(pdf_table_to_json(pdf_path))
