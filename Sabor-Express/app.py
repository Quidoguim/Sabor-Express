import os


class GerenciadorRestaurantes:
    def __init__(self):
        self.restaurantes = []

    def cadastrar_restaurante(self, nome, tipo):
        novo_restaurante = {"nome": nome, "tipo": tipo, "status": False}
        self.restaurantes.append(novo_restaurante)

    def ativar_restaurante(self, nome):
        for restaurante in self.restaurantes:
            if restaurante["nome"].lower() == nome.lower():
                restaurante["status"] = not restaurante["status"]
                return restaurante["status"]

    def buscar_restaurante(self, nome):
        for restaurante in self.restaurantes:
            if restaurante["nome"].lower() == nome.lower():
                return restaurante

    def listar_restaurantes(self):
        return self.restaurantes


gerenciador = GerenciadorRestaurantes()


def exibir_nome_app():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


def exibir_menu():
    print('1. Cadastrar Restaurante.')
    print('2. Ativar/Desativar Restaurante.')
    print('3. Listar Restaurantes.')
    print('4. Sair.\n')


def encerrar_app():
    exibir_texto('Encerrando aplicação...')


def voltar_menu():
    input('Pressione ENTER para voltar ao menu...')
    main()


def menu_incorreto():
    print('Opção inválida. Tente novamente.\n')
    exibir_menu()
    menu_escolhido()


def exibir_texto(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_novo_restaurante():
    exibir_texto('Cadastrar novo restaurante:')

    nome = input('Nome: ')
    tipo = input('Tipo: ')

    gerenciador.cadastrar_restaurante(nome, tipo)

    print(f'Restaurante "{nome}" cadastrado como tipo "{tipo}" com sucesso!\n')
    voltar_menu()


def ativar_restaurante():
    exibir_texto(
        'Digite o nome do restaurante que deseja ativar ou desativar:')
    nome = input('Nome: ').strip()

    restaurante = gerenciador.buscar_restaurante(nome)

    if restaurante is None:
        print(f'Restaurante "{
              nome}" não encontrado. Certifique-se de que o nome está correto.\n')
        return voltar_menu()

    status_atual = "Ativo" if restaurante["status"] else "Desativado"
    print(f'O restaurante "{
          restaurante["nome"]}" está atualmente: {status_atual}')
    print('Digite "1" para ativar ou "2" para desativar.')

    status = input('Opção: ')

    if status == '1' and not restaurante["status"]:
        gerenciador.ativar_restaurante(nome)
        print(f'Restaurante "{nome}" foi ativado com sucesso!\n')
        voltar_menu()
    elif status == '2' and restaurante["status"]:
        gerenciador.ativar_restaurante(nome)
        print(f'Restaurante "{nome}" foi desativado com sucesso!\n')
        voltar_menu()
    elif status == '1' and restaurante["status"]:
        print(f'O restaurante "{nome}" já está ativo!\n')
        voltar_menu()
    elif status == '2' and not restaurante["status"]:
        print(f'O restaurante "{nome}" já está desativado!\n')
        voltar_menu()
    else:
        print('Opção inválida. Tente novamente.\n')
        voltar_menu()


def listar_restaurantes():
    exibir_texto('Listando restaurantes...')

    restaurantes = gerenciador.listar_restaurantes()

    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        for restaurante in restaurantes:
            status = "Ativo" if restaurante["status"] else "Desativado"
            print(f'O restaurante "{restaurante["nome"]}" está cadastrado como tipo "{
                restaurante["tipo"]}" e está "{status}".')

    print()
    voltar_menu()


def menu_escolhido():
    try:
        menu_escolhido = int(input('Escolha uma opção: '))

        if menu_escolhido == 1:
            print(f'Você escolheu a opção {menu_escolhido}.\n')
            cadastrar_novo_restaurante()
        elif menu_escolhido == 2:
            print(f'Você escolheu a opção {menu_escolhido}.\n')
            ativar_restaurante()
        elif menu_escolhido == 3:
            print(f'Você escolheu a opção {menu_escolhido}.\n')
            listar_restaurantes()
        elif menu_escolhido == 4:
            encerrar_app()
        else:
            menu_incorreto()
    except ValueError:
        menu_incorreto()


def main():
    os.system('cls')
    exibir_nome_app()
    exibir_menu()
    menu_escolhido()


if __name__ == '__main__':
    main()
