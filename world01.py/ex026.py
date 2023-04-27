#procura string
n = input('Digite uma frase: ')
n = n.lower()
serc = 'a'
n1 = n.count(serc)
print(n1)
n2 = n.find(serc)
n3 = n.rfind(serc)
print(n2)
print(n3)