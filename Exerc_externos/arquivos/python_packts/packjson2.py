from urllib.request import urlopen
import json
# "http://vimeo.com/api/v2/video/57733101.jason"

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")

dados = json.loads(response)[0] #obs> quando tiro o [0] da erro, certamente é pelo fato de que o 0 indica que estou querendo o conteúdo da chave, 




print('titulo', dados['title'])
print('Url', dados['url'])
print('Duração', dados['duration'])
print('User name', dados['user_name'])




