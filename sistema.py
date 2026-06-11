from lib.interface import *
from lib.arquivo import *


arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (['ver pessoas cadastradas', 'cadastrar nova pessoa', 'sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('saindo do sistema... até logo !')
        break
    else:
        print('ERRO ! Digite uma opção valida!')