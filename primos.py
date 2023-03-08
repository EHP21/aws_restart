

inicio = 1
tope = 250


for numero in range (inicio, tope+1  ):  
    if numero >1:  
        for i in range (2, numero):  
            if (numero % i) == 0:  
                break  
        else:  
            with open('TEXTO2.txt', 'a') as my_file:
             my_file.write(str(numero)+"\n")