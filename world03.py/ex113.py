#reescreva a função leiaint() que criamos no desafio N° 104  incluindo agora a possibilidade da digitação de um número invalido
#aproveite agora e também crie uma função leiafloat()
#######################################################################################################################

def leiaint(num):
    while True:
        valor = str(num)
        valor = valor.isnumeric()
        if valor == True:
            resp = int(num) 
            return f'O valor digitado foi \033[1;36m{resp}\033[m'
            break    
        else:
            resp = num
            print(f'\n\033[1;31mErro!\033[m \n\033[1;36m->\033[m \033[1;33m{resp}\033[m \033[1;36m<-\033[m \n\033[1;31mNão é um número inteiro!\033[m')
            num = input('\nDigite um número inteiro: ')     
    
        
def leiadecimal(num):
    while True:
        valor = num
        subs = num.replace('.','0')
        vnum = subs.isdigit()
        if vnum == True and '.' in valor:
            return f'O valor digitado foi \033[1;36m{valor}\033[m'
            break
        else:
            print(f'\n\033[1;31mErro!\033[m \n\033[1;36m->\033[m \033[1;33m{valor}\033[m \033[1;36m<-\033[m \n\033[1;31mNão é um número decimal!\033[m')
            num = input('\nDigite um número decimal: ')     
    
        
    




x = input('Digite um número inteiro: ')
print(leiaint(x))

z =input('\nDigite um número decimal:')
print(leiadecimal(z))