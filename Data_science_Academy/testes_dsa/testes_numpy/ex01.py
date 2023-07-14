import numpy as dsa

#array numpy criado
arr01 = dsa.array((10,12,13,15,22,37))


#metodo soma de numpy em ação para achar a media de forma manual
soma= dsa.sum(arr01)
mediaf = soma/6
print("media manual: ",mediaf)


#achando media de uma array com numpy
print(dsa.mean(arr01))