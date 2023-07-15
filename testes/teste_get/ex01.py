
cache= {}

def pega(url):
    if cache.get(url):
        return cache[url]
    else:
        dado = url
        cache[url] = dado
        return dado
    


while True:
    x = int(input("Digite um núemro: "))
    if x == 0:
        break
    print(pega(x))

    print(cache)
   