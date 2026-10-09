import sys 
from database.connection import init_db
from module.auth import criar_usuario_admin_padrao, autenticar_usuario, Session

def main():
    print("Iniciando o Sistema de Vendas...")


    #1. Inicializar o banco de dados (cria as tabelas se não existem)
    init_db()

    #2. Cria o usuario administrador padrão caso o banco esteja vazio
    criar_usuario_admin_padrao()

    print("\n"+ "="*30)
    print("     SISTEMA DE VENDAS v1.0")
    print("="*30)

    #loop de login
    while True:
        print("\n --- LOGIN --- ")
        login= input("Usúario: ")
        senha= input("Senha: ")

        sucesso, msg = autenticar_usuario(login, senha)

        if sucesso:
            print(f"\n[SUCESSO] {msg}")
            menu_principal()
            break
        else:
            print(f"\n[ERRO] {msg}")
            tentar_novamente= input("Deseja tentar novamente? (S/n): ").strip().lower()
            if tentar_novamente == "n":
                print("Encerrando o sistema...")
                sys.exit(0)

def menu_principal():
    while True:
        print("\n"+"="*30)
        print("     MENU PRINCIPAL")
        print("="*30)
        print(f"Usúario Logado: {Session.nome} | Cargo: {Session.cargo}")
        print("-"*30)
        print("1. Cadastrar Produto (Em breve)")
        print("2. Nova Venda (Em breve)")
        print("3. Relatórios (Em breve)")
        print("0. Sair")

        opcao= input("\n Escolha uma opção: ").strip()
        if opcao == '0':
            print("Saindo do sistema... Até logo!")
            Session.clear()
            sys.exit(0)
        elif opcao in ['1','2','3']:
            print(f"\n[Aviso] A funcionalidade '{opcao}' ainda não foi implementada")
        else:
            print("\n[ERRO] Opção invalida!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Sistema encerrado pelo usúario")
        sys.exit(0)
