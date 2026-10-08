import sys 
from database.connection import init_db
from modules.auth import criar_usuario_admin_padrao, autenticar_usuario, Session 

def main():
    print("Iniciando o sistema de vendas...")
    #1. Inicializando o banco de dados (cria as tabelas se não existirem)
    init_db()
    #2. Cria o usuario administrador padrão caso o banco esteja vazio
    criar_usuario_admin_padrao()

    print("\n" + "="*30)
    print("    SISTEMA DE VENDAS v1.0")
    print("="*30)

    #loop de login
    while True:
        print("\n---LOGIN---")
        login= input("Usúario: ")
        senha= input("Senha: ")

        sucesso, msg= autenticar_usuario(login,senha)

        if sucesso:
            print(f"\n[SUCESSO] {msg}")
            menu_principl()
            break
    else:
        print(f"\n[ERRO] {msg}")
        tentar_novamente= input("Deseja tentar novamente? (S/n): ").strip().lower()
        if tentar_novamente== 'n':
            print("Encerrando o sistema...")
            sys.exist(0)


def menu_principal():
    while True:
        print("\n"+"="*30)
        print("     MENU PRINCIPAL")
        print("="*30)
        print(f"Usúario LOgando: {Session.nome} | Cargo: {Session.cargo}")
        print("-"*30)
        print("1. Cadastrar Produto {Em breve}") 
        print("2. Nova Venda (Em breve)")
        print("3. Relatorio (Em breve)")
        print("0. Sair")

        opcão= input("\n EScolha uma opção: ").strip()
        if opcão == '0':
            print("Saindo do sistema... Até logo!")
            Session.clear()
            sys.exit(0)
            