num = int(input("Ingresa un numero\n"))
tem=""
for i in range(11):
    tem += f"{num} + {i} = {num*i} \n"

print(tem)