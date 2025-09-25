<h1 align="center">💰 Gerenciador de Finanças Pessoais</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License Badge"/>
  <img src="https://img.shields.io/badge/Status-Finalizado-success.svg" alt="Status Badge"/>
</p>

<p align="center">
  Aplicativo <strong>desktop em Python</strong> para controle financeiro pessoal com interface gráfica.<br>
  O sistema permite gerenciar transações, gerar relatórios e visualizar gráficos de forma <strong>intuitiva e profissional</strong>.
</p>

---

## 📖 Sobre o Projeto  

O **Gerenciador de Finanças Pessoais** foi desenvolvido com foco em **organização, simplicidade e clareza visual**.  
Com ele, você pode cadastrar transações, armazená-las em arquivo, analisar relatórios mensais e visualizar gráficos que ajudam a compreender melhor sua vida financeira.  

---

## 🚀 Funcionalidades  

- ➕ **Cadastro de transações** (valor, categoria, tipo, descrição)  
- 💾 **Armazenamento automático em CSV**  
- 📊 **Relatórios detalhados por mês e ano**  
- 🥧 **Gráficos de pizza interativos** integrados à interface  
- 🖼️ **Interface gráfica responsiva** com Tkinter  
- 🎨 **Visual minimalista e funcional**  

---




## 🛠️ Tecnologias Utilizadas  

- **Python 3.11+**  
- **Tkinter** → Criação da interface gráfica  
- **Matplotlib** → Gráficos estatísticos  
- **PyInstaller** → Geração de executáveis (.exe)  

---

## ⚙️ Como Executar  

1. Clone o repositório:  
```bash
git clone https://github.com/okingsaam/gerenciador-financas.git
cd gerenciador-financas
````
2. Instale as dependências::pip install matplotlib
```
pip install matplotlib
```
---
📂 Estrutura do Projeto
```
gerenciador-financas/
├── interface.py              # Interface principal do sistema
├── finance/
│   ├── transaction.py        # Classe responsável pelas transações
│   └── report.py             # Classe para geração de relatórios
├── data/
│   └── transactions.csv      # Base de dados em CSV
```
---
📦 Criar Executável (.exe)
```
pyinstaller --onefile --windowed interface.py
```
---
📌 Roadmap (Possíveis Melhorias)

 Exportar relatórios em PDF e Excel

 Filtro de transações por categoria e intervalo de datas

 Novos gráficos: linha, barras comparativas

 Integração com SQLite/MySQL

 Adição de tema escuro (Dark Mode)
 ---
 ```
 🧑‍💻 Autor

Feito com dedicação e visão por Douglas Santos (King Sam)
📍 Salvador - BA, Brasil

📬 Contato:

🐙 GitHub: okingsaam

💼 LinkedIn: Douglas Santos

✉️ Email: okingsaam@gmail.com
```
---

Esse modelo já tem cara de **projeto de desenvolvedor profissional**, com:  
✔️ Estrutura clara  
✔️ Layout moderno  
✔️ Seções bem distribuídas  
✔️ Roadmap (mesmo sendo finalizado, mostra visão de evolução)  

👉 Quer que eu monte também um **banner personalizado em imagem** (com seu nome, título e ícones de tecnologias) pra colocar no topo do README? Isso dá um diferencial enorme no GitHub.
