TOTAL = 10
CONT = 1

while CONT <= TOTAL:
    nome = input("Nome: ")
    n1 = float(input("Nota da primeira prova: "))
    n2 = float(input("Nota da segunda prova: "))
    media = (n1 + n2)/ 2
    if media >= 7:
        print(f"O aluno {nome} foi aprovado com media {media}")
    else:
        print(f"O aluno {nome} foi reprovado com media {media}")
    CONT += 1
print("**** Finalizado ****")