import tkinter as tk
from tkinter import messagebox
from finance.transaction import adicionar_transacao
from finance.report import gerar_relatorio_por_mes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# 🎯 Janela principal
janela = tk.Tk()
janela.title("Gerenciador de Finanças")
janela.geometry("520x720")
janela.resizable(False, False)

canvas_pizza = None  # usado para limpar gráfico anterior

# 📊 Gráfico de pizza
def mostrar_grafico_pizza(relatorio):
    global canvas_pizza

    if canvas_pizza:
        canvas_pizza.get_tk_widget().destroy()

    categorias = list(relatorio.keys())
    valores = [abs(v) for v in relatorio.values()]

    if not categorias or sum(valores) == 0:
        return

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
    ax.set_title("Distribuição por categoria")

    canvas_pizza = FigureCanvasTkAgg(fig, master=janela)
    canvas_pizza.draw()
    canvas_pizza.get_tk_widget().grid(row=11, columnspan=2, pady=10)

# 💸 Adicionar transação
def adicionar():
    try:
        valor = float(entry_valor.get())
        categoria = entry_categoria.get().strip()
        tipo = tipo_var.get()
        descricao = entry_descricao.get().strip()

        if not categoria or not tipo or not descricao:
            raise ValueError("Preencha todos os campos.")

        adicionar_transacao(valor, categoria, tipo, descricao)
        messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")

        entry_valor.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# 📅 Gerar relatório
def gerar_relatorio():
    try:
        mes = int(entry_mes.get())
        ano = int(entry_ano.get())
        relatorio = gerar_relatorio_por_mes(mes, ano)

        if not relatorio:
            resultado = "Nenhuma transação encontrada para esse período."
        else:
            resultado = f"📅 Relatório de {mes:02d}/{ano}:\n"
            for categoria, saldo in relatorio.items():
                tipo = "Receita" if saldo >= 0 else "Despesa"
                resultado += f"- {categoria}: R$ {abs(saldo):.2f} ({tipo})\n"

        text_relatorio.delete("1.0", tk.END)
        text_relatorio.insert(tk.END, resultado)

        mostrar_grafico_pizza(relatorio)

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível gerar o relatório.\n{e}")

# 🧱 Layout
tk.Label(janela, text="Valor (R$):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_valor = tk.Entry(janela)
entry_valor.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Categoria:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_categoria = tk.Entry(janela)
entry_categoria.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Tipo:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tipo_var = tk.StringVar(value="despesa")
tk.OptionMenu(janela, tipo_var, "receita", "despesa").grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Descrição:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_descricao = tk.Entry(janela)
entry_descricao.grid(row=3, column=1, padx=10, pady=5)

tk.Button(janela, text="Adicionar Transação", command=adicionar, bg="#4CAF50", fg="white").grid(row=4, columnspan=2, pady=10)

tk.Label(janela, text="Mês:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_mes = tk.Entry(janela)
entry_mes.grid(row=5, column=1, padx=10, pady=5)

tk.Label(janela, text="Ano:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_ano = tk.Entry(janela)
entry_ano.grid(row=6, column=1, padx=10, pady=5)

tk.Button(janela, text="Gerar Relatório", command=gerar_relatorio, bg="#2196F3", fg="white").grid(row=7, columnspan=2, pady=10)

tk.Label(janela, text="Resumo:").grid(row=8, columnspan=2, padx=10, pady=5)
text_relatorio = tk.Text(janela, height=10, width=50)
text_relatorio.grid(row=9, columnspan=2, padx=10, pady=5)

# 🚀 Inicia a interface
janela.mainloop()
