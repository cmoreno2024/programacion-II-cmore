# Calculadora de IMC
def calculadora_IMC (peso,altura):
    imc = peso / (altura ** 2)
    return imc
def clasificar_imc(imc):
    if imc < 18.5:
        return "usted esta por debajo del peso normal"
    elif imc >= 18.5 and imc < 25 :
        return"su peso es normal"
    elif imc >= 25 and imc < 30 :
        return "usted tiene sobrepeso"
    else:
        return "usted tiene obesidad"
#ejemplo de uso
peso = float(input("ingrese su peso en kg:"))
altura = float(input("ingrese su altura en metros:"))
imc = calculadora_IMC(peso,altura)
print("su imc es:",imc)
print(clasificar_imc(imc))


#Analizador de numeros 
def analizaror(numero):
    resultado = {}
    resultado["par"]= numero%2 == 0
    if numero > 0:
        resultado["+"]= "positivo"
    elif numero < 0:
        resultado["-"]= "negativo"
    else:
        resultado["0"]= "cero"
    resultado["divisible_por_3"]= numero%3 == 0
    resultado["divisible_por_5"]= numero%5 == 0
    resultado["divisible_por_3_5"]= numero%3 == 0 and numero%5 ==0
    return resultado

#ejemplo de uso
numero_ejemplo= int(input("por favor ingrese un numero: "))
print(analizaror(numero_ejemplo))


#Calculadora de área y perímetro de figuras geométricas:
def calcular_area_cuadrado(lado):
    return lado ** 2
def calcular_perimetro_cuadrado(lado):
    return lado * 4
def calcular_area_rectangulo(base,altura):
    return base * altura
def calcular_perimetro_rectangulo(base,altura):
    return 2 * (base + altura)
def calcular_area_circulo(radio):
    return 3.1416 * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio
def calcular_area_triangulo(base,altura):
    return (base * altura) / 2
def calcular_perimetro_triangulo(a,b,c):
    return a + b + c
#ejemplo de uso
print("Calculadora de área y perímetro de figuras geométricas")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Círculo")
print("4. Triángulo")
figura = int(input("ingrese la figura que desea calcular: "))
if figura == 1:
    lado = float(input("ingrese el lado del cuadrado: "))
    print("El área del cuadrado es: ", calcular_area_cuadrado(lado))
    print("El perímetro del cuadrado es: ", calcular_perimetro_cuadrado(lado))
elif figura == 2:
    base = float(input("ingrese la base del rectángulo: "))
    altura = float(input("ingrese la altura del rectángulo: "))
    print("El área del rectángulo es: ", calcular_area_rectangulo(base,altura))
    print("El perímetro del rectángulo es: ", calcular_perimetro_rectangulo(base,altura))
elif figura == 3:
    radio = float(input("ingrese el radio del círculo: "))
    print("El área del círculo es: ", calcular_area_circulo(radio))
    print("El perímetro del círculo es: ", calcular_perimetro_circulo(radio))
else: 
    a = float(input("ingrese el lado a del triángulo: "))
    b = float(input("ingrese el lado b del triángulo: "))
    c = float(input("ingrese el lado c del triángulo: "))
    base = float(input("ingrese la base del triángulo: "))
    altura = float(input("ingrese la altura del triángulo: "))
    print("El área del triángulo es: ", calcular_area_triangulo(base,altura))
    print("El perímetro del triángulo es: ", calcular_perimetro_triangulo(a,b,c))

















