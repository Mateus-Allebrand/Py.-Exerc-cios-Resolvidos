#Programa lê um angulo e retona para o usuário o seno , cosseno e tangenete desse angulo.


#Programa principal
import math
ang = int(input('Digite o angulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno é {:.2f} , o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tan))
x = math.radians