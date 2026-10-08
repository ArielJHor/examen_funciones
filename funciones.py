def validador(lista):
    hola=[]
    for i in lista:
        if i==int:
            if i>2010:
                hola.append(True)
            elif i>=100 and i<300:
                hola.append(True)
            else:
                hola.append(False)
    return hola