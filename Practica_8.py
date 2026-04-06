texto_prueba_1 = "Hola, hola mundo! Este mundo es un mundo genial. ¿Genial, no?"
texto_prueba_2 = "Mate, mate, ¡siempre mate! Un buen mate con jengibre, es un buen MATE. ¿Mate o café? Mate."

sin_comillas = texto_prueba_2.replace("," , "").replace( "?" , "").replace("!" , "").replace("¿" , "").replace("¡" , "")
sin_mayus = sin_comillas.lower()
final = sin_mayus.split()


diccionario = {}

for palabra in final:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else: diccionario[palabra] = 1 

print(diccionario)