def leiadinheiro(valor):
    val = str(input(valor))
    vf = val.isnumeric()
    if vf == True:
        resp = int(val)
    while vf == False:
        print('Erro! Digite apenas valores monetários!')
        val = str(input('Digite um valor: R$'))
        vf = val.isnumeric()
        if vf == True:
            resp = int(val)
            break
        
    return resp
            








