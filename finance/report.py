import csv
from datetime import datetime
from collections import defaultdict

def gerar_relatorio():
    resumo = defaultdict(float)
    try:
        with open("data/transactions.csv", mode="r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            for linha in leitor:
                data, valor, categoria, tipo, descricao = linha
                valor = float(valor)
                if tipo.lower() == "receita":
                    resumo[categoria] += valor
                elif tipo.lower() == "despesa":
                    resumo[categoria] -= valor
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    return resumo

def gerar_relatorio_por_mes(mes, ano):
    resumo = defaultdict(float)
    try:
        with open("data/transactions.csv", mode="r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            for linha in leitor:
                data, valor, categoria, tipo, descricao = linha
                valor = float(valor)
                data_obj = datetime.strptime(data, "%Y-%m-%d")
                if data_obj.month == mes and data_obj.year == ano:
                    if tipo.lower() == "receita":
                        resumo[categoria] += valor
                    elif tipo.lower() == "despesa":
                        resumo[categoria] -= valor
    except Exception as e:
        print(f"Erro ao gerar relatório por mês: {e}")
    return resumo
