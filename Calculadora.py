#CALCULADORA
#Calculadora de operaciones basicas mediante un menú simple
import math
def separ():
    print("***************************************")

#suma
def suma ():
    x= (float(input("Valor: ")))
    y= (float(input("mas: ")))
    suma=x+y
    
    with open("calculadora.txt","a")as archivo:
        archivo.write(f'{x} entre {y} es = {suma}')
        archivo.write("\n*************************************************************\n")

#resta
def resta ():
    x= (float(input("Valor: ")))
    y= (float(input("menos: ")))
    rest=x-y

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'{x} entre {y} es ={rest}')
        archivo.write("\n*************************************************************\n")

#multipliaccion
def multi ():
    x= (float(input("Valor: ")))
    y= (float(input("por: ")))
    mult=x*y

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'{x} por {y} es ={mult}')
        archivo.write("\n*************************************************************\n")

#division 
def divis ():
    x= (float(input("Valor: ")))
    y= (float(input("Entre: ")))
    div=x/y

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'{x} entre {y} es = {div} ')
        archivo.write("\n*************************************************************\n")

#exponente
def expon ():
    x=(int(input("\"e\" elevado a:  ")))
    eelv = math.exp (x)

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'base de logaritmo natural a la {x} es = {eelv} ')
        archivo.write("\n*************************************************************\n")
        
#factorial
def fact ():
    x=(float(input("factorial de: ")))
    factor = math.factorial(x)
    with open("calculadora.txt","a")as archivo:
        archivo.write(f'factorial de {x} es = {factor} ')
        archivo.write("\n*************************************************************\n")

#Potencia
def pot():
    x=(float(input("valor: ")))
    y=(float(input("elevada a la potencia: ")))
    poten = math.pow(x,y)

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'{x} elevada a la potencia {y} es = {poten}')
        archivo.write("\n*************************************************************\n")

#Raiz cuadrada
def rcuad():
    x=(float(input("raiz cuadrada de: ")))
    raiz = math.isqrt(x)

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'raiz cuadrada de {x} es = {raiz}')
        archivo.write("\n*************************************************************\n")


#Raiz cuibica
def rcub ():
    x=(float(input("raiz cubica de: ")))
    raizc = math.cbrt(x)

    with open("calculadora.txt","a")as archivo:
        archivo.write(f'raiz cubica de {x} es = {raizc}')
        archivo.write("\n*************************************************************\n")

#razones trigonometricas
def razonesT ():
    print("1.Seno \ 2.Coseno \ 3.Tangente ")
    op=(int(input("ingrese la opcion: ")))

    #seno
    if op == 1:
        x=(float(input("seno de: ")))
        sen=math.sin(x)

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'Seno de: {x} es = {sen} radianes')
            archivo.write("\n*************************************************************\n")

    #coseno
    elif op==2:
        x=(float(input("coseno de: ")))
        sen=math.cos(x)

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'Coseno de: {x} es = {sen} radianes')
            archivo.write("\n*************************************************************\n")
    
    #tangente
    elif op==3:
        x=(float(input("tangente de: ")))
        tang=math.tan(x)

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'Tangennte de: {x} es = {tang} radianes')
            archivo.write("\n*************************************************************\n")

#Area de una figura: triagulo resctangulo, circulo, cuadrado
def areasF ():

    print("a)Triangulo \ b)Rectangulo \n c)Circulo \ d)Cuadrado ")
    op=(input("ingrese la opcion: "))

    #triangulo
    if op == 'a' or op == 'A':
        x=(float(input("base: ")))
        y=(float(input("altutra: ")))
        area=(x*y)/2

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'base ({x}) por altura ({y}) entre 2 = {area}')
            archivo.write("\n*************************************************************\n")

    #rectagulo
    elif op == 'b' or op == 'B':
        x=(float(input("base: ")))
        y=(float(input("altutra: ")))
        area=x*y

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'base ({x}) por altura ({y}) es = {area}')
            archivo.write("\n*************************************************************\n")

        
    
    #circulo
    elif op == 'c' or op == 'C':
        pi=math.pi
        radio=(float(input("ingrese el radio: ")))
        area=pi*(radio**2)

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'pi ({pi}) por radio ({radio}) al cuadrado es = {area}')
            archivo.write("\n*************************************************************\n")

    #cuadrado    
    elif op == 'd' or op == 'D':
        x=(float(input("medida del lado: ")))
        area=x*x

        with open("calculadora.txt","a")as archivo:
            archivo.write(f'lado ({x}) por lado ({x}) es = {area}')
            archivo.write("\n*************************************************************\n")

def menu():
    print("                  MENÚ")
    separ()
    print("[1]Suma")
    print("[2]Resta")
    print("[3]Multipliación")
    print("[4]Divsion")
    print("[5]Euler Exponente")
    print("[6]Factorial")
    print("[7]Potencia")
    print("[8]Raiz Cuadrada")
    print("[9]Raiz Cubica")
    print("[10]Razones Trigonometricas")
    print("[11]Areas de Figuras")
    print("[12]Salir")
    separ()


print("CALCULADORA")
separ()
menu()
opc=int(input("Ingresa el numero corresponfiente a la opcion quedeseas realizar: "))
separ()
while opc != 12 :
    if opc==1:
        suma()
    elif opc==2:
        resta()
    elif opc==3:
        multi()
    elif opc==4:
        divis()
    elif opc==5:
        expon()
    elif opc==6:
        fact()
    elif opc==7:
        pot()
    elif opc==8:
        rcuad()
    elif opc==9:
        rcub()
    elif opc==10:
        razonesT()
    elif opc==11:
        areasF()
    elif opc==12:
        break
    else:
        print("no existe esa opcion, ingresa una correcta\n")

    menu()
    opc=int(input("Ingresa el numero corresponfiente a la opcion quedeseas realizar: "))
