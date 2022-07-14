import pandas as pd
import openpyxl
from Tools.scripts.dutree import display

while True:
    try:
        imposto = float(input('Qual a porcentagem de imposto no preço do produto? '))
        break
    except:
        print('Valor inválido.\n')

def add_imposto(preco, imposto=imposto):
    mult = 1 + (imposto/100)
    return preco * mult


while True:
    try:
        arq = str(input('Digite o nome do arquivo: ')) + '.xlsx'
        break
    except:
        print('Opção incorreta.')

try:
    tabela = pd.read_excel(arq)
    while True:
        try:
            nome_coluna = str(input('Qual o nome da sua nova coluna? '))
            coluna_tabela = str(input('Qual o nome da coluna com os dados que você quer usar? '))
            tabela[nome_coluna] = list(map(add_imposto, tabela[coluna_tabela]))
            print(tabela)
            nomenovo = str(input('Qual o nome do novo arquivo? '))
            tabela.to_excel(f'{nomenovo}.xlsx')
            print(f'O arquivo {nomenovo} foi criado com sucesso.')
            break
        except:
            print(f'A coluna não existe.')
except:
    print('Erro: Tente novamente.')







