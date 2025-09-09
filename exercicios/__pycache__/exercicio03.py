def tente(idade_txt: str)->None:
    try:
        idade = int(idade_txt)
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente")
        print(f"Idade registrada: {idade}")
    except ValueError:
        print("Entrada inválida, tente novamente.")

def menor_que_50(valor):
    if not(valor>50):
        print(f"\nValor = {valor}")

if __name__ == "__main__":
    texto = input("Digite sua idade: ")
    n = int(input("Informe um valor número inteiro: "))
    tente(texto)
    menor_que_50(n)