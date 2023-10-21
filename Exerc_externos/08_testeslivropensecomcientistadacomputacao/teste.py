#exercícios1.2

#1.Quantos segundos há em 42 minutos e 42 segundos?

tot_segundos = (42 * 60) + 42

print(f'Total de segundo em 42 minutos e 42 segundos é {tot_segundos}\n')

#2.Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

milhas = 10/1.6

print(f'Total de milhas em 10 quilometros = {milhas}')


#3.Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?


velocidade = 10000/ tot_segundos 

metros_milha = 1609.34
milhapsegundo = metros_milha/velocidade

print(f'velocidade media de {velocidade:.2f} m/s\ntempo por milha em segundo é de {milhapsegundo:.2f}\ntempo por milha em minutoo é de {milhapsegundo/60 :.2f} ')


