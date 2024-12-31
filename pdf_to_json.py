import camelot
import json
import sys

def pdf_table_to_json(pdf_path):
    # Extrair tabelas do PDF
    tables = camelot.read_pdf(pdf_path, pages='all')
    
    # Lista para armazenar todas as transações
    transacoes = []
    
    # Processar cada tabela
    for table in tables:
        # Converter a tabela para uma lista de dicionários
        table_data = table.df.to_dict(orient='records')
        
        # Ignorar o cabeçalho (primeiro item) e processar as transações
        for row in table_data:
            # Criar o dicionário no formato desejado
            transacao = {
                "DESCRIÇÃO": row["0"],
                "DATA": row["1"],
                "HORA": row["2"],
                "VALOR": row["3"],
                "SALDO": row["4"],
                "CARTÃO": row["5"]
            }
            # Adicionar à lista de transações
            transacoes.append(transacao)
    
    # Retornar as transações em formato JSON
    return json.dumps(transacoes, ensure_ascii=False)

if __name__ == '__main__':
    # Verificar se o caminho do PDF foi passado como argumento
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_json.py <pdf_path>")
        sys.exit(1)
    
    # Caminho do PDF passado como argumento
    pdf_path = sys.argv[1]
    
    # Converter o PDF para JSON e imprimir o resultado
    print(pdf_table_to_json(pdf_path))
