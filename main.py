from finance.report import gerar_relatorio_por_mes

relatorio_mes = gerar_relatorio_por_mes(9, 2025)
print("\n📅 Resumo de Setembro 2025:")
for categoria, saldo in relatorio_mes.items():
    tipo = "Receita" if saldo >= 0 else "Despesa"
    print(f"- {categoria}: R$ {abs(saldo):.2f} ({tipo})")
