def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        

def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'novo registro de {nome} adcionado!')
            a.close()


def leiaint(num):
    while True:
        valor = str(num)
        valor = valor.isnumeric()
        if valor == True:
            resp = int(num) 
            return resp
            break    
        else:
            resp = num
            print(f'\n\033[1;31mErro!\033[m \n\033[1;36m->\033[m \033[1;33m{resp}\033[m \033[1;36m<-\033[m \n\033[1;31mNão é um número inteiro!\033[m')
            num = input('\nDigite um número inteiro: ')   