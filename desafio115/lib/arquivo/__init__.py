from desafio115.lib.interface import*

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')# significa abrir pra leiturato
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')#significa escreve o arquivo de texto se nao existe ele cria usando (+)
        a.close()
    except:
        print('houve um erro na criação de um arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')
    finally:
        a.close()


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', ' ')
            print(f'{dados[0]:<30}{dados[1]:>3}anos')
    finally:
        a.close()


def cadastra(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')#at significa append para acrescentar item a lista de arquivos de texto
    except:
        print('houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
