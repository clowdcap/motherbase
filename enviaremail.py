import win32com.client as win32
import auth


def enviar_email():
    # criar integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # criar um email
    email = outlook.CreateItem(0)

    # configurar as informações
    email.To = ''
    email.Subject = ''

    if email.To == '':
        email.To = str(input('Para quem vai esse e-mail? '))

    if email.Subject == '':
        email.Subject = str(input('Qual o assunto do e-mail? '))

    # variváveis
    nome = str(input('Nome: '))
    sobrenome = str(input('Sobrenome: '))

    if nome == '' and sobrenome == '':
        nome = 'Senhor'
        sobrenome = '(a)'
    if nome == '' and sobrenome != '':
        nome = 'Sr (a).'

    # adicionando anexo
    def anexar_documento(nome_arquivo):
        if nome_arquivo == '':
            anexo = ''
            if nome_arquivo == '':
                nome_arquivo = str(input('Qual o nome do arquivo?: '))
                if nome_arquivo != '':
                    anexo = fr'C:\Users\clowd\Documents\Python Scripts\motherbase\anexo\{nome_arquivo}'
        else:
            anexo = fr'C:\Users\clowd\Documents\Python Scripts\motherbase\anexo\{nome_arquivo}'

        if anexo == '':
            print('Sem Anexo...')
        else:
            email.Attachments.Add(anexo)
            print('Anexado documento...')

    # css
    css = '''
        <style>
                    * {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }

                    body {
                        width: 100%;
                        overflow-x: hidden;
                    }

                    .email {
                        margin: 2%;
                    }

                    .topo {
                        padding: 0.3rem 0; 
                        background-color: brown;
                        width: 100%;
                        text-align: center !important;
                        margin-bottom: 35px;
                        font-family: Arial, Helvetica, sans-serif;
                    }

                    .topo h2 {
                        font-size: 28px;
                        color: white;
                        padding-top: 25px;
                    }

                    img {
                        width: 80px;
                        height: 80px;
                    }

                    .capa {
                        text-align: center;
                        width: 100%;
                        padding: 0.5rem 0;
                        background-color: cadetblue;
                    }
                    .capa p {
                        font-size: 16px;
                        font-family: Arial, Helvetica, sans-serif;
                        color: white;
                        text-align: left !important;
                        padding: 0 30px;
                    }

                    .conteudo {
                        text-align: center;
                        width: 100%;
                        padding: 2rem;
                        background-color: gainsboro;
                    }

                    .conteudo p{
                        font-size: 20px;
                        font-family: Arial, Helvetica, sans-serif;
                    }

                    .conteudo p a {
                        text-decoration: none;
                        color: red;
                    }

                    .assinatura {
                        background-color: royalblue;
                        color: white;
                        font-family: Arial, Helvetica, sans-serif;
                        margin-top: 20px;
                        padding: 2%;
                    }
                </style>
        '''

    # body

    print('Qual tipo de conteudo você gostaria de mandar')
    print('[1] - Conclusao de Analise Técnica\n[2] - Carimbo Padrao PMCM \n[3] - Sair')
    escolha_conteudo = int(input('Digite o valor numérico: '))

    if escolha_conteudo == 1:
        # Entro em contato referente as Analise Técnicas do Protocolo:
        protocolo = str(input('Qual o Protocolo / Ano: '))
        conteudo = f'''
            <div class="conteudo">
                            <p>Bom dia {nome} {sobrenome},</p>
                            <br>


                            <p>Entro em contato referente as Análises Técnicas do Protocolo: {protocolo}</p> 
                            <br>


                            <p>Todas as correçôes foram feitas e todos os requisitos para proceguimento da aquisiçãodo 
                            alvará de construção foram atentidas ! </p> 
                            <br>

                            <p>Qualquer dúvida ou atualização de situação, entre em contato</p> 
            </div>
            '''
    elif escolha_conteudo == 2:
        nome_arquivo = 'legenda-pmcm.dwg'
        anexar_documento(nome_arquivo)
        conteudo = f'''
        <div class="conteudo">
                        <p>Bom dia {nome} {sobrenome},</p>
                        <br>


                        <p>Entro em contato para atender a sua solicitação</p> 
                        <br>


                        <p>Está anexado a esse mensagem, um arquivo em dwg, onde o mesmo contém a estrutura de 
carimbo padrão da prefeitura, logo, a tabela de estatística está junto.</p> 
                        <br>

                        <p>Nome do arquivo: <b>{nome_arquivo} </b></p>
                        <p>Tamanho do arquivo: <b>75,3 KB</b></p>

                        <p>Caso eu não tenha esclarecido totalmente a sua dúvida, estou à disposição</p>


        </div>
        '''
    elif escolha_conteudo == 3:
        print('Ok, fechando aplicação\nRetornando ao menu do sistema')
        auth.auth()

    assinatura = '''
         <div class="assinatura">
            <p>Atenciosamente,</p>
                <br>
                <br>
            <h3>Jose Marinho</h3>
                <br>
            <p><a style="color: white;" href="https://wa.me/qr/LQM5O2QPPRDOH1">Whatsapp: (41) 9 9272-5388</a></p>
            <p>Telefone: (41) 3677-4050 - Setor Urbanismo</p>
            <p>jm.arquiteturacwb@gmail.com</p>
            <p>Prefeitura Municipal de Campo Magro / PR</p>
        </div>
        '''

    topo = '''
        <div class="topo">
            <img src="https://leismunicipais.com.br/img/cidades/pr/campo-magro.png" alt="campo-magro">
            <h2>Prefeitura Municipal de Campo Magro</h2>
        </div> <!--topo-->
        '''

    capa = '''
        <div class="capa">
            <p>Atendimento via E-mail - A/C: <b>José Marinho - Estagiário</b></p>
        </div> <!--capa-->
        '''

    email.HTMLBody = f'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                {css}
            </head>
            <body>
                <section class="email">

                    {topo}

                    {capa}

                    {conteudo}

                    {assinatura}

                </section>
            </body>
        </html>

        '''

    # finalizando email
    email.Send()
    print('Email enviado !')
    print(auth.separar)
    print('Você gostaria de voltar ao menu ?')
    print('[1] - Não')
    retornar_menu_email = int(input('Digite o valor numérico: '))

    if retornar_menu_email == 1:
        print('Ok, reiniciando calculadora')
    elif retornar_menu_email == 2:
        print('Ok, fechando aplicação\nRetornando ao menu do sistema')
        auth.auth()
