from desafio115.lib.interface import *
from desafio115.lib.arquivo import*
from time import sleep

arq = 'Curso em Video.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['Ver pessoa cadastradas', 'Cadastra pessoas', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resp == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastra(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO! digite uma opção valida!\033[m')
    sleep(2)
