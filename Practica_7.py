palabra = "Hola mundo"
resultado = ""
numero = (len(palabra))

for i in range (0 , numero ):
    resultado += (palabra[-i - 1])

print(resultado)    