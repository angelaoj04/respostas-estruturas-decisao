n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if(n1 > n2 and n1 > n3):
    print("Número 1 é o maior: ", n1)
elif(n2 > n1 and n2 > n3):
    print("Número 2 é o maior: ", n2)
elif(n3 > n2 and n3 > n1):
    print("Número 3 é o maior: ", n3)