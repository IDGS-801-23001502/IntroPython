
def numRepeat(my_list:list):
    list_result=[]
    for i in my_list:
        item = my_list.count(i)
        list_result.append(f"{i} repetido {item} veces")
    return list(set(list_result))

lista=[]
for i in range(20):
    lista.append(int(input(f"Ingresa un numero (pueden ser repetidos)\n")))

lista.sort()
print("Lista ordenada\n",lista)
print("Numeros repetidos","\n".join(map(str, numRepeat(lista))))
print("Lista separada en pares e impares\n",
      "Pares:\n", 
      list(filter(lambda x: x % 2 == 0, lista)),
      "\n\nImpares:\n", 
      list(filter(lambda x: x % 2 != 0, lista)))

