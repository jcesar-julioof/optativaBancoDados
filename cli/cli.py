import database

def exibir_menu():
    print("\n--- SISTEMA CLI ---")
    print("[1] Incluir")
    print("[2] Listar Tudo")
    print("[3] Pesquisar por Código")
    print("[4] Pesquisar por Nome")
    print("[5] Alterar")
    print("[6] Excluir")
    print("[0] Sair")
    return input("Escolha uma opcao: ")

def main():
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            print("\n[ INCLUSAO ]")
            nome = input("Nome: ")
            descricao = input("Descricao: ")
            database.incluir(nome, descricao)
            print("Registro incluido com sucesso.")

        elif opcao == '2':
            print("\n[ LISTAGEM ]")
            registros = database.listar_todos()
            for r in registros:
                print(f"Codigo: {r[0]} | Nome: {r[1]} | Descricao: {r[2]}")

        elif opcao == '3':
            print("\n[ PESQUISA POR CODIGO ]")
            try:
                codigo = int(input("Digite o codigo: "))
                r = database.buscar_por_codigo(codigo)
                if r:
                    print(f"Codigo: {r[0]} | Nome: {r[1]} | Descricao: {r[2]}")
                else:
                    print("Registro nao encontrado.")
            except ValueError:
                print("Codigo invalido.")

        elif opcao == '4':
            print("\n[ PESQUISA POR NOME ]")
            nome = input("Digite o nome: ")
            registros = database.buscar_por_nome(nome)
            if registros:
                for r in registros:
                    print(f"Codigo: {r[0]} | Nome: {r[1]} | Descricao: {r[2]}")
            else:
                print("Nenhum registro encontrado.")

        elif opcao == '5':
            print("\n[ ALTERACAO ]")
            try:
                codigo = int(input("Codigo do registro a alterar: "))
                if database.buscar_por_codigo(codigo):
                    novo_nome = input("Novo nome: ")
                    nova_descricao = input("Nova descricao: ")
                    database.alterar(codigo, novo_nome, nova_descricao)
                    print("Registro alterado.")
                else:
                    print("Registro nao existe.")
            except ValueError:
                print("Codigo invalido.")

        elif opcao == '6':
            print("\n[ EXCLUSAO ]")
            try:
                codigo = int(input("Codigo do registro a excluir: "))
                if database.buscar_por_codigo(codigo):
                    confirmacao = input("Tem certeza que deseja excluir? (S/N): ").strip().upper()
                    if confirmacao == 'S':
                        database.excluir(codigo)
                        print("Registro excluido.")
                    else:
                        print("Operacao cancelada.")
                else:
                    print("Registro nao existe.")
            except ValueError:
                print("Codigo invalido.")

        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")

if __name__ == '__main__':
    main()
