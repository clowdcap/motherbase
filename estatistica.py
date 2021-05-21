import auth


def apresentar_calculadora():
    print('Bem vindo(a) à calculadora de estatisticas')
    print('A seguir, preencha todos os campos')
    coletar_estatistica()


def coletar_estatistica():
    # Informações principais
    area_do_terreno = float(input('1 - Área do terreno: '))
    print('---' * 30)
    area_anteriormente_construido = float(input('2 - Área anteriormente construido: '))
    print('---' * 30)
    area_computavel_subsolo = float(input('3 - Área computável a construir no subsolo: '))
    print('---' * 30)
    area_nao_computavel_subsolo = float(input('4 - Área não computável a construir no subsolo: '))
    print('---' * 30)
    area_computavel_terreo = float(input('5 - Área computável a construir no pavimento térreo: '))
    print('---' * 30)
    area_nao_computavel_terreo = float(input('6 - Área não computável a construir no pavimento térreo: '))
    print('---' * 30)
    area_computavel_superior = float(input('7 - Área computável a construir no pavimento superior: '))
    print('---' * 30)
    area_nao_computavel_sup = float(input('8 - Área não computável a construir no pavimento superior: '))
    print('---' * 30)

    # informações complementares
    area_nao_computavel_atico = float(input('9 - Área não computável a construir no ático: '))
    print('---' * 30)

    # Informações principais
    area_livre = float(input('10 - Área livre: '))
    print('---' * 30)

    # Informações complementares
    num_pavimento = int(input('11 - Número de pavimentos: '))
    print('---' * 30)
    altura_total = float(input('12 - Altura total: '))
    print('---' * 30)
    area_cobertura = float(input('22 - Área de cobertura: '))
    print('---' * 30)

    def calcular_estatistica():
        projecao_edificacao = area_anteriormente_construido + area_computavel_terreo + area_nao_computavel_terreo
        print('13 - Projeção da Edificação: {:.2f}m²'.format(projecao_edificacao))
        print('---' * 30)
        taxa_ocupacao = (projecao_edificacao / area_do_terreno) * 100
        print('14 - Taxa de Ocupação: {:.2f}%'.format(taxa_ocupacao))
        print('---' * 30)
        taxa_permeabilidade = (area_livre / area_do_terreno) * 100
        print('15 - Taxa de Permeabilidade: {:.2f}%'.format(taxa_permeabilidade))
        print('---' * 30)
        area_total_contruir_subsolo = area_computavel_subsolo + area_nao_computavel_subsolo
        print('16 - Área total a construir no subsolo: {}m²'.format(area_total_contruir_subsolo))
        print('---' * 30)
        area_total_contruir_terreo = area_computavel_terreo + area_nao_computavel_terreo
        print('17 - Área total a construir no pavimento térreo: {}m²'.format(area_total_contruir_terreo))
        print('---' * 30)
        area_total_contruir_superior = area_computavel_superior + area_nao_computavel_sup
        print('18 - Área total a construir no pavimento superior: {:.2f}m²'.format(area_total_contruir_superior))
        print('---' * 30)
        area_total_contruir_computavel = area_computavel_subsolo + area_computavel_terreo + area_computavel_superior
        print('19 - Área total a construir computável: {}m²'.format(area_total_contruir_computavel))
        print('---' * 30)
        area_total_contruir_nao_computavel = area_nao_computavel_subsolo + area_nao_computavel_terreo + area_nao_computavel_sup
        print('20 - Área total a construir não computável: {}m²'.format(area_total_contruir_nao_computavel))
        print('---' * 30)
        coeficiente_aproveitamento = (
                (area_total_contruir_computavel + area_anteriormente_construido) / area_do_terreno)
        print('21 - Coeficiente de aproveitamento: {:.4f}'.format(coeficiente_aproveitamento))
        print('---' * 30)
        area_total_construida_liberada = area_total_contruir_computavel + area_total_contruir_nao_computavel
        print('23 - Área total construída a ser liberada: {}m²'.format(area_total_construida_liberada))

    calcular_estatistica()
    print('\n')
    print('Gostaria de calcular as estatísticas novamente ?')
    print('[1] - Calcular novamente\n[2] - Voltar ao menu')
    calc_novamente = int(input('Digite o valor numérico: '))

    if calc_novamente == 1:
        print('Ok, reiniciando calculadora')
        apresentar_calculadora()
    elif calc_novamente == 2:
        print('Ok, fechando aplicação\nRetornando ao menu do sistema')
        auth.auth()
