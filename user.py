# AINDA EM MANUTENCAO

# AINDA FORA DE ATIVIDADE

import auth


l_usuario = ['Jose', 'admin']
l_senha = ['jose', 'senha123']


def adicionar_usuario():
    usuario = str(input("Digite o nome de usuário:"))
    if usuario in l_usuario:
        print('Usuário já está cadastrado')
    else:
        l_usuario.append(usuario)
        senha = str(input("Digite a senha:"))
        l_senha.append(senha)
        print('Usuário cadastrado')
        auth.iniciar_sistema()


def remover_usuario():
    usuario = str(input("Digite o nome do usuário:"))
    if usuario in l_usuario:
        l_usuario.remove(usuario)
        print('Usuário Removido')
    else:
        print('Esse usuário não está cadastrado')
    pass
