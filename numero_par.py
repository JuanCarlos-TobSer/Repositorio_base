'''Pedir dos numeros y determinar cual es par,
o si ambos lo son.'''

num1 = int(input("Digite primer numero: "))
num2 = int(input("Digite segundo numero: "))

if num1%2==0 and num2%2==0:
	print("Ambos numeros son pares")
elif num1%2==0:
	print("El primer numero es par")
elif num2%2==0:
	print("El segundo numero es par")
else:
	print("Ambos numeros son impares")