numeros = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
primos = []
for i in range (1 , 101):
    variable = i
    for numero in numeros:
        if variable % numero == 0:
            primos.append(i)

print(primos)