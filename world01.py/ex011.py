#calculador de tinta
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
tinta = float(input('Quantos m² a tinta pinta por litro? '))
lata = float (input('a Lata possui quantos litros de tinta? '))
m2parede = largura * altura 
rendetinta = tinta * lata
nlatast = m2parede / rendetinta
print('tem {:.2f} m² de parede para pintar, precisará de {:.2f} latas de tinta.'.format(m2parede, nlatast))