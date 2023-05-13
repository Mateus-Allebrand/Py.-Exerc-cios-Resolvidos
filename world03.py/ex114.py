#teste se um site esta disponivel na internet com python
import urllib.request
try:
    site= urllib.request.urlopen('http://www.pudim.com.br')
except Exception as e:
    print("Servidor indisponível. Erro:")
else:
    print('Consegui acessar o site pudim cm sucesso!')