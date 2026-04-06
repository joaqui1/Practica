lista = [0 , 1]
for i in range (2 , 50):
    fibo = []
    fibo = lista[i - 1] + lista[i - 2]
    lista.append(fibo)
    print(fibo)