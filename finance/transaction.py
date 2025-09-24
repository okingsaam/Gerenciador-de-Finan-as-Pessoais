import csv
from datetime import datetime

def adicionar_transacao(valor, categoria, tipo, descricao):
    with open("data/transactions.csv", mode="a", newline='') as arquivos:
        escritor = csv.writer(arquivos)
        data_atual = datetime.now().strftime("%Y-%m-%d")
        escritor.writerow([data_atual, valor, categoria, tipo, descricao])
if __name__ == "__main__":
    adicionar_transacao(123.45, "teste", "receita", "teste direto")
    print("Módulo executado com sucesso!")
