import enviaremail
import user
import estatistica
import info

# Variaveis globais
separar = '=' * 20
finalizar_sistema = '\nFinalizando Sistema'


def iniciar_sistema():
    print('\nLogin Sistema')
    usuario = str(input('Login: '))
    senha = str(input('Senha: '))
    confere_login(usuario, senha)


def confere_login(usuario, senha):
    conferido = False
    conferido_user = False
    conferido_senha = False

    if usuario == 'admin' and senha == 'senha123':
        print('Login autorizado \n')
        conferido_user = True
        conferido_senha = True
    else:
        print('Senha ou Login incorreto \n')
        conferido = False
        iniciar_sistema()

    if conferido_user and conferido_senha:
        conferido = True

    if conferido:
        auth()


def auth():

    enviar_email = False
    print('\nSelecione as opções de ferramentas')
    print('[1] - Mandar E-Mail \n[2] - Calculadora de Estatística\n[3] - Cadastrar Usuario')
    print('[4] - Remover Usuario \n[5] - Listar Usuarios\n[6] - Sair ')
    escolha_ferramenta = int(input('Digite o valor numérico: '))

    def mandar_email_auth():
        global enviar_email
        print('\nQuer mandar email ?\n[1] - Sim\n[2] - Não')
        solicitar_email = str(input('Digite o valor numérico: '))
        if solicitar_email == 1:
            auth_enviar_email = True

            if auth_enviar_email:
                enviar_email = True
            else:
                print('Erro ao autorizar enviar e-mail')
                print('Saindo do Sistema de Login')
                central()

            if enviar_email:
                enviaremail.enviar_email()
        elif solicitar_email != 1:
            print('Saindo do Sistema de Login')
            print(separar)
            auth()

    if escolha_ferramenta == 1:
        print('Mandar E-mail ...\nCarregando...\nPrograma carregado com sucesso!')
        mandar_email_auth()
        enviaremail.enviar_email()
    elif escolha_ferramenta == 2:
        print('Calculadora de Estatística ...\nCarregando...\nPrograma carregado com sucesso!')
        estatistica.apresentar_calculadora()
    elif escolha_ferramenta == 6:
        print('Voltando sistema inicial\n')
        central()


def central():
    print(separar)
    print('Ola, seja bem vindo à MotherBase')
    print('Lista de Aplicação \n[1] - Login\n[2] - Creditos\n[3] - Sair')
    central_escolha = int(input('Digite o valor numérico: '))

    if central_escolha == 1:
        iniciar_sistema()
    elif central_escolha == 2:
        info.creditos_sistema()
        central()
    else:
        print(finalizar_sistema)
