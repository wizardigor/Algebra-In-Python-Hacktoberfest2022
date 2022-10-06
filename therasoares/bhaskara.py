import math

print("Benvinde a calculadora de Bhaskara\n Vamos te ajudar a descobrir os valores de X\n")
print("Para começarmos insira os valores da sua equação\n exemplo: ax2 + bx +c = 0\n")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = (b*b)-4*(a*c)
b2= b*b
print(b2)

x1 = (-b+math.sqrt(delta))/(2*a)
x2 = (-b-math.sqrt(delta))/(2*a)

print("Delta = ", delta)
print("+X = ", x1)
print("-X = ", x2)
