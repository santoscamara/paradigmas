def ordem(a: int, b: int, c: int)->None:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(f"\n1º valor: {a}")
    print(f"2º valor: {b}")
    print(f"3º valor: {c}")

if __name__ == "__main__":
    a = int(input("Informe o 1º valor: "))
    b = int(input("Informe o 2º valor: "))
    c = int(input("Informe o 3º valor: "))
    ordem(a,b,c)