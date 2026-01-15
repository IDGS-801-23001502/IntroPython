import os

def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a,b):
    return a+b

os.system("cls")
#saludar("Ana")
os.system("pause")

def main():
    saludar("Juan")
    resultado_suma = sumar(5,7)
    print("La suma de 5 + 7 es:", resultado_suma)

if __name__ == "__main__":
    main()