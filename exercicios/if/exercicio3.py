try:
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))

    if num1 < num2:
        crescente = (num1, num2)
        decrescente = (num2, num1)
    else:
        crescente = (num2, num1)
        decrescente = (num1, num2)

    print(f"\nCrescente: {crescente[0]}, {crescente[1]}")
    print(f"Decrescente: {decrescente[0]}, {decrescente[1]}")

except ValueError:
    print("Erro: Deve introduzir números inteiros válidos.")