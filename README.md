# 💰 Gerenciador de Finanças Pessoais  

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)  
![Status](https://img.shields.io/badge/Status-Finalizado-green)  

Aplicativo **desktop em Python** para controle financeiro pessoal com interface gráfica.  
Permite adicionar transações, gerar relatórios mensais e visualizar gráficos interativos — tudo de forma simples e intuitiva.  

---

## 🚀 Funcionalidades  

- ➕ Adição de transações (valor, categoria, tipo, descrição)  
- 💾 Armazenamento automático em CSV  
- 📊 Relatório por mês e ano  
- 🥧 Gráfico de pizza embutido na interface  
- 🖼️ Interface gráfica com Tkinter  
- 🎨 Visual limpo e responsivo  

---

## 🎥 Demonstração  

> *(Adicione aqui um gif ou screenshot do app rodando)*  

![Screenshot](screenshot.png) <!-- substitua com sua imagem ou gif -->

---

## 🛠️ Tecnologias utilizadas  

- **Python 3.11+**  
- **Tkinter**  
- **Matplotlib**  
- **PyInstaller** (opcional, para gerar `.exe`)  

---

## 📦 Como executar  

1. Clone o repositório:  
```bash
git clone https://github.com/okingsaam/gerenciador-financas.git
cd gerenciador-financas
````
2.Instale as dependências:
```
pip install matplotlib
````
3.python interface.py
```
python interface.py
````
🧱 Estrutura do projeto
```
gerenciador-financas/
├── interface.py
├── finance/
│   ├── transaction.py
│   └── report.py
├── data/
│   └── transactions.csv
```
📦 Gerar executável (.exe)
```
pyinstaller --onefile --windowed interface.py
```
## ✨ Autor  

Feito com 💻 e visão por **Douglas (King Sam)**  
📍 Salvador, Bahia  

📬 **Contato:**  
- 🐙 [GitHub: okingsaam](https://github.com/okingsaam)  
- 💼 [LinkedIn: Douglas Santos](https://www.linkedin.com/in/douglas-santos-30257a327/)  

