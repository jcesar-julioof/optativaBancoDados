import tkinter as tk
from tkinter import ttk, messagebox
import database

class SistemaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema CRUD")
        self.root.geometry("600x400")

        # Sistema de Abas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.aba_inclusao = ttk.Frame(self.notebook)
        self.aba_listagem = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_inclusao, text="[+] Incluir")
        self.notebook.add(self.aba_listagem, text="[=] Listar / Gerenciar")

        self.construir_aba_inclusao()
        self.construir_aba_listagem()

    def construir_aba_inclusao(self):
        ttk.Label(self.aba_inclusao, text="Nome:").pack(pady=(20, 5))
        self.entry_nome = ttk.Entry(self.aba_inclusao, width=40)
        self.entry_nome.pack()

        ttk.Label(self.aba_inclusao, text="Descricao:").pack(pady=5)
        self.entry_descricao = ttk.Entry(self.aba_inclusao, width=40)
        self.entry_descricao.pack()

        ttk.Button(self.aba_inclusao, text="Salvar Registro", command=self.salvar_inclusao).pack(pady=20)

    def construir_aba_listagem(self):
        # Frame superior para pesquisa
        frame_top = ttk.Frame(self.aba_listagem)
        frame_top.pack(fill='x', pady=5, padx=5)

        ttk.Label(frame_top, text="Buscar:").pack(side='left', padx=5)
        self.entry_busca = ttk.Entry(frame_top, width=20)
        self.entry_busca.pack(side='left', padx=5)
        
        ttk.Button(frame_top, text="Pesquisar Nome/Cod", command=self.pesquisar).pack(side='left', padx=5)
        ttk.Button(frame_top, text="Mostrar Tudo", command=self.carregar_tabela).pack(side='left', padx=5)

        # Tabela (Treeview)
        colunas = ('codigo', 'nome', 'descricao')
        self.tabela = ttk.Treeview(self.aba_listagem, columns=colunas, show='headings')
        self.tabela.heading('codigo', text='Codigo')
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('descricao', text='Descricao')
        
        self.tabela.column('codigo', width=50)
        self.tabela.column('nome', width=200)
        self.tabela.column('descricao', width=300)
        self.tabela.pack(fill='both', expand=True, padx=5, pady=5)

        # Frame inferior para ações
        frame_bottom = ttk.Frame(self.aba_listagem)
        frame_bottom.pack(fill='x', pady=5, padx=5)

        ttk.Button(frame_bottom, text="Alterar Selecionado", command=self.alterar_selecionado).pack(side='left', padx=5)
        ttk.Button(frame_bottom, text="Excluir Selecionado", command=self.excluir_selecionado).pack(side='right', padx=5)

        self.carregar_tabela()

    # -- Funcoes de Acao --

    def salvar_inclusao(self):
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        
        if not nome or not descricao:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        database.incluir(nome, descricao)
        messagebox.showinfo("Sucesso", "Registro incluido.")
        self.entry_nome.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.carregar_tabela()

    def carregar_tabela(self, registros=None):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        if registros is None:
            registros = database.listar_todos()
            
        for r in registros:
            self.tabela.insert('', 'end', values=r)

    def pesquisar(self):
        termo = self.entry_busca.get()
        if not termo:
            self.carregar_tabela()
            return
            
        if termo.isdigit():
            r = database.buscar_por_codigo(int(termo))
            self.carregar_tabela([r] if r else [])
        else:
            r = database.buscar_por_nome(termo)
            self.carregar_tabela(r)

    def excluir_selecionado(self):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um registro na tabela.")
            return
            
        item = self.tabela.item(selecao[0])
        codigo = item['values'][0]
        
        if messagebox.askyesno("Confirmacao", f"Excluir registro codigo {codigo}?"):
            database.excluir(codigo)
            self.carregar_tabela()

    def alterar_selecionado(self):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um registro na tabela.")
            return
            
        item = self.tabela.item(selecao[0])
        codigo = item['values'][0]
        nome_atual = item['values'][1]
        desc_atual = item['values'][2]

        # Cria janela secundaria para edicao
        janela_edicao = tk.Toplevel(self.root)
        janela_edicao.title("Alterar Registro")
        
        ttk.Label(janela_edicao, text="Novo Nome:").pack(pady=5)
        entry_n = ttk.Entry(janela_edicao, width=30)
        entry_n.insert(0, nome_atual)
        entry_n.pack(padx=10)

        ttk.Label(janela_edicao, text="Nova Descricao:").pack(pady=5)
        entry_d = ttk.Entry(janela_edicao, width=30)
        entry_d.insert(0, desc_atual)
        entry_d.pack(padx=10)

        def salvar_edicao():
            database.alterar(codigo, entry_n.get(), entry_d.get())
            janela_edicao.destroy()
            self.carregar_tabela()

        ttk.Button(janela_edicao, text="Salvar Alteracoes", command=salvar_edicao).pack(pady=15)

if __name__ == '__main__':
    root = tk.Tk()
    app = SistemaGUI(root)
    root.mainloop()
