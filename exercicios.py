'''Leia uma string com um texto completo e devolva um dicionário contendo as palavras
e sua frequência'''
def conta_palavras(texto):
    dicionario = {}
    texto = texto.split()

    for palavras in texto:
        if palavras in dicionario:
            dicionario[palavras] += 1
        else:
            dicionario[palavras] = 1

    print(dicionario)

# conta_palavras("caraca caraca que coisa legal caraca que que que uma vez a a a a a a")

'''Crie uma função que receba o nome completo de uma pessoa e devolva o primeiro e
o último nomes, mais as iniciais do meio.
Exemplo: EDSON ARANTES SOARES DO NASCIMENTO -> EDSON A S NASCIMENTO'''

def abrevia_nome(nome_completo):
    nome_completo = nome_completo.split(" ")
    primeiro_nome = nome_completo[0]
    ultimo_nome = nome_completo[-1]
    nomes_do_meio = nome_completo[1:-1]
    iniciais = []
    for nomes in nomes_do_meio:
        if len(nomes) > 3:
            iniciais.append(nomes[0])
    abreviacoes = " ".join(iniciais)
    return "{} {} {}".format(primeiro_nome, abreviacoes, ultimo_nome)



print(abrevia_nome("João Vitor dos Santos"))

'''Função que recebe uma data no formato “dd/mm/aaaa” e devolve uma string contendo a
data por extenso. Usa um dicionário para converter o número do mês no seu nome.
 data_extenso(“12/10/2013”)-> “12 de outubro de 2013”
 data_extenso(“29/07/1995”)-> “29 de julho de 1995”
 '''
def data_extenso(data):
    data = data.split('/')
    dia = data[0]
    mes = data[1]
    ano = data[2]
    lista = {'01': 'Janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril',
             '05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto', '09': 'setembro',
             '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
    # print(lista[mes])

    return "{} De {} De {}".format(dia, lista[mes], ano)

'''Questão 4 '''
def ler(arquivo):
    file = open(arquivo).readlines()
    return file

def separar(arquivo):
    # print(arquivo)
    fiados = {}
    for nomes in arquivo:
        nome, valor = nomes.split(";")
        valor = valor.replace("\n", "")
        valor = float(valor)
        try:
            fiados[nome] += valor
        except:
            fiados[nome] = valor
    return fiados