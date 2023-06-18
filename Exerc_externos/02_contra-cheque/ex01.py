# Faça um programa que pergunte quanto o profissional ganha por hora e 
# quantas horas é trabalhada por mês, calcule e mostre o salário no referedi mês
# descontado 11% Imposto de renda
# descontado 8% inss 
# descontado 5% sindicato 

# mostre todos os dados para o funcionário

#Variáveis
forma = dict()


#Impostos
ir = 11/100
inss = 8/100
sind = 5/100

#Dados de entrada
nome = input("Olá,\nQual seu nome? ").title()
print(f"Bem vindo! {nome}")
valorh = float(input(f"Qual o valor da sua hora trabalhada em R$? "))
tothmes = float(input("Quantas horas tu trabalha por mês? "))


#calculos
forma['Valor Bruto'] = valbruto = tothmes * valorh
ir *= valbruto 
forma['Desc. Imposto de renda'] = ir
inss *= valbruto
forma['Desc. Inss'] = inss
sind *= valbruto
forma['Desc. Sindicato'] = sind
totdesc = (ir + inss + sind)
forma['Total Desc.'] = totdesc
valiq = valbruto - totdesc
forma['Valor liquido'] = valiq


#saida de dados
print("\n")
print("==== CONTRA-CHEQUE ====".center(50))

for i in forma:
    print(f"{i:<30}  R$ {forma[i]:>10.2f}")







#Analise de tabulação (Ex. 95 world 3)
# for t,i in enumerate(time):
#         print(f' {t:<2}        {i["nome"]:<10}                         {i["total_gols"]:<8}')
#     print('==-=='*10)
#     r = str(input('Deseja ver dados de algum jogador em particular? [S/N]')).upper()[0]
#     while r not in 'SN':
#         print('ERRO! Responda apenas com [S] ou [N]')
#         r = str(input('Deseja ver dados de algum jogador em particular? [S/N]')).upper()[0]
#     if r == 'N':
#         print('              == -> FIM! <- ==')
#         break
#     cod = int(input('Digite o código: '))
#     print()
#     print(time[cod])