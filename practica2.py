
def suma(a,b):
    print(a+b) 

def resta(a,b):
    print(a-b) 

def multiplicar(a,b):
    print(a*b) 

def dividir(a,b):
    print(a/b) 

def main():
    num1=int(input("Ingresa el primer numero\n"))
    num2=int(input("Ingresa el segundo numero\n"))
    eleccion = int(input("Selecciona una opcion: \n1.-Sumar \n2.-Restar\n3.-Dividir\n4.-Dividir\n5.-Salir\n"))

    match eleccion:
        case 1:
            suma(num1,num2)
        case 2:
            resta(num1,num2)
        case 3:
            multiplicar(num1,num2)
        case 4:
            dividir(num1,num2)

if __name__ == "__main__":
    main()