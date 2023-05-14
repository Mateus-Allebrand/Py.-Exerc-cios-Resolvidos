#crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de testo simples
#O sistema deve ter duas opções cadastrar e listar todas as pessoas cadastradas.
###############################################################################################################
from modulos import menu
from arquivo import arquivoexiste
from arquivo import criararquivo
from arquivo import lerarquivo


arq = 'ex15.txt'
if not arquivoexiste(arq):
   criararquivo(arq)


menu()
