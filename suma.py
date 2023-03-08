

cuenta_negativos = 0
suma_positivos = 0
for i in range (1, 7):
    print ('ingresa el valor ' + repr (i))
    un_numero = int (input (' '))
    if un_numero>0:
        i=+1
        suma_positivos=((suma_positivos+un_numero)/i)
    if un_numero<0:
        cuenta_negativos=cuenta_negativos+un_numero
    print ()
print ('La suma de los negativos es: ' + repr (cuenta_negativos))
print (' El promedio de los positivos es: ' + repr (suma_positivos))