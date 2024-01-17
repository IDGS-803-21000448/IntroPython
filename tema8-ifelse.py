
num1 = int(input("Dame el valor de n1: "))
num2 = int(input("Dame el valor de n2: "))


if num1 > num2:

    print("El {} es mayor que el {}".format(num1, num2))
else:
     print("El {} es mayor que el {}".format(num2, num1))


print("----------------------------- Dmae Una Edad ---------------------------")
edad = int(input("Ingresa tu eddad: "))

if edad > 18:
     print("Eres Mayor de edad")
elif edad == 19:
     print("Tienes 18")
else:
     print("Eres Menor De Edad")

