# utf-8
# exercício 115
from Ex0115.lib.arquivo import *
from Ex0115.lib.interface import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('SISTEMA ARQUIVO v1.0')
while True:
    verif = False
    menu()
    linha()
    opcao = Leiaint('Sua opção: ')
    if opcao == 1:
        # Opcao de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif opcao == 2:
        # Opcao de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        insert(arq, input(str('Digite o nome: ')), Leiaint('Digite a idade: '))
    elif opcao == 3:
        print('Saindo do sistema...Até logo!')
        verif = True
    else:
        print('\33[0;31mErro! Por favor informe um número válido.\33[m')
    if verif:
        break
