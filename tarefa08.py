p1 = float(input("Informe o valor do primeiro Produto: "))
p2 = float(input("Informe o valor do segundo Produto: "))
p3 = float(input("Informe o valor do terceiro Produto: "))

if(p1 < p2 and p1 < p3):
    print("Você deve comprar o produto 1 de valor R$", p1)
elif(p2 < p1 and p2 < p3):
    print("Você deve comprar o produto 2 de valor R$", p2)
elif(p3 < p2 and p3 < p1):
    print("Você deve comprar o produto 3 de valor R$", p3)