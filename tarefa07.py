n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

maior = 0
menor = 0

if n1>n2 and n1>n3:
    maior = n1
    if n2<n3:
        menor = n2
    else:
        menor = n3
elif n2>n1 and n2>n3:
    maior = n2
    if n1<n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n1<n2:
        menor = n1
    else:
        menor = n2

print("Maior númer: ", maior)
print("Menor numero ", menor)