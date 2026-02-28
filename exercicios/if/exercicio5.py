try:
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    num3 = int(input("Introduza o terceiro número: "))

    # Criar lista com os números
    numeros = [num1, num2, num3]

    # Ordem crescente
    crescente = sorted(numeros)

    # Ordem decrescente
    decrescente = sorted(numeros, reverse=True)

    print(f"\nCrescente: {crescente[0]}, {crescente[1]}, {crescente[2]}")
    print(f"Decrescente: {decrescente[0]}, {decrescente[1]}, {decrescente[2]}")

except ValueError:
    print("Erro: Deve introduzir números inteiros válidos.")