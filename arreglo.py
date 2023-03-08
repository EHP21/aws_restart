
print ('ingresa el numero de valores que vas a capturar ')
cantidad = int (input (' '))
max_value = None
max_idx = None

numeros = []
for i in range(cantidad):
    
    numero = input(f"Ingresa el número {i + 1}: ")
    # Se convirtio a entero Convertir a entero,
    numero = int(numero)
    # Se agrego al arreglo con  append
    numeros.append(numero)

for idx, num in enumerate(numeros):
    if (max_value is None or num > max_value):
        max_value = num
        max_idx = idx
        print('El valor maximo es :', max_value)