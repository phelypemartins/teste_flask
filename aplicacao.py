def minha_aplicacao():

  import tkinter as tk
  from tkinter import messagebox
  from tkinter import ttk
  import mysql.connector
  from mysql.connector import Error
  from datetime import datetime

  def criar_conexao():
      try:
          conexao = mysql.connector.connect(
              host='192.168.1.22',
              database='pessoal',
              user='felipe',
              password='00241100'
          )
          return conexao
      except Error as e:
          messagebox.showerror("Erro", f"Erro ao conectar ao MySQL: {e}")
          return None

  def inserir_dados():
      valor = valor_entry.get()
      forma_pagamento = forma_pagamento_var.get()
      
      vencimento = data_vencimento_entry.get()
      data_vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
      vencimento_convertido = data_vencimento.strftime("%Y-%m-%d")
      
      pagamento = data_pagamento_entry.get()
      data_pagamento = datetime.strptime(pagamento, "%d/%m/%Y")
      pagamento_convertido = data_pagamento.strftime("%Y-%m-%d")

      conexao = criar_conexao()
      if conexao:
          cursor = conexao.cursor()
          sql = "INSERT INTO pessoal.Vendas (valor, forma_pagamento, vencimento, pagamento) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, (valor, forma_pagamento, vencimento_convertido, pagamento_convertido))
          conexao.commit()
          cursor.close()
          conexao.close()
          messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
          valor_entry.delete(0, tk.END)
          data_vencimento_entry.delete(0, tk.END)
          data_pagamento_entry.delete(0, tk.END)

  def fetch_data(start_date, end_date):
      conexao = criar_conexao()
      if conexao:
          cursor = conexao.cursor()
          query = "SELECT * FROM pessoal.Vendas WHERE vencimento >= %s AND vencimento <= %s"
          cursor.execute(query, (start_date, end_date))
          rows = cursor.fetchall()
          cursor.close()
          conexao.close()
          return rows
      return []

  def show_data():
      start_date = entry_start_date.get()
      end_date = entry_end_date.get()
      
      for row in tree.get_children():
          tree.delete(row)
      
      # Converter as datas para o formato correto
      start_date = datetime.strptime(start_date, "%d/%m/%Y").strftime("%Y-%m-%d")
      end_date = datetime.strptime(end_date, "%d/%m/%Y").strftime("%Y-%m-%d")

      data = fetch_data(start_date, end_date)
      
      for row in data:
          tree.insert("", "end", values=row)

  # Criando a interface gráfica
  app = tk.Tk()
  app.geometry("1680x1050")
  app.title("Formulário")

  # Campos para inserção de dados
  tk.Label(app, text="Valor:").pack(pady=5)
  valor_entry = tk.Entry(app)
  valor_entry.pack(pady=5)

  forma_pagamento_var = tk.StringVar(app)
  forma_pagamento_var.set("Escolha uma forma de pagamento")

  formas_pagamento = ["PIX", "Dinheiro", "Cartão de Crédito"]
  forma_pagamento_menu = tk.OptionMenu(app, forma_pagamento_var, *formas_pagamento)
  forma_pagamento_menu.pack(pady=5)

  tk.Label(app, text="Vencimento").pack(pady=5)
  data_vencimento_entry = tk.Entry(app)
  data_vencimento_entry.pack(pady=5)

  tk.Label(app, text="Pagamento").pack(pady=5)
  data_pagamento_entry = tk.Entry(app)
  data_pagamento_entry.pack(pady=5)

  tk.Button(app, text="Registrar", command=inserir_dados).pack(pady=20)

  # Campos para busca de dados
  tk.Label(app, text="Data Inicial (dd/mm/yyyy):").pack(pady=5)
  entry_start_date = tk.Entry(app)
  entry_start_date.pack(pady=5)

  tk.Label(app, text="Data Final (dd/mm/yyyy):").pack(pady=5)
  entry_end_date = tk.Entry(app)
  entry_end_date.pack(pady=5)

  tk.Button(app, text="Buscar Dados", command=show_data).pack(pady=20)

  # Criar a tabela
  tree = ttk.Treeview(app, columns=("valor", "forma_pagamento", "vencimento", "pagamento"), show='headings')
  tree.heading("valor", text="Valor")
  tree.heading("forma_pagamento", text="Forma de Pagamento")
  tree.heading("vencimento", text="Vencimento")
  tree.heading("pagamento", text="Pagamento")
  tree.pack(pady=20, fill='both', expand=True)

  app.mainloop()

  return "Aplicacao Executada"