from funciones import validador
lista=["Horen", 2010, 180, "Graffigna", 2011, 165, "Ciafrelli", 2011, 176, "Campos", 2010, 182]
list2=validador(lista)
for n in range(len(list2)):
    if n//2==0:
        if list2==True:
            print("Nacio en 2010 o mas?")
            if list2==False:
                print("no nacio en 2010 o mas?")
    else:
        if list2==True:
            print("su altura esta en 180 cm o mas?")
            if list2==False:
                print("su altura no esta en 180 cm o mas?")