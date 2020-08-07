nota1 = float(input("Informe a primeira nota: "))

nota2 = float(input("Informe a segunda nota: "))

media = (nota1+nota2)//2
print(media)

if(media >= 7 and media < 10):
    print("Aluno aprovado!")
elif(media == 10):
    print("Aluno aprovado com distinção!")
elif(media < 7):
    print("Aluno reprovado!")
