def script_calcula_nota(nome: str, nota1: float, nota2: float) -> None:
    media = (nota1 + nota2)/2
    if media < 0:
        print(f"Média negativa, média inválida {media}")
    elif media >= 7.0 and media <= 10.0:
        print(f"O aluno {nome} foi aprovado com media {media:.1f}")
    elif media < 7.0:
        print(f"O aluno {nome} foi reprovado com media {media:.1f}")
    else:
        print("Média Inválida")

if __name__ == "__main__":
    nome=str(input("Digite seu nome: "))
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    script_calcula_nota(nome,nota1,nota2)

