try:
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    num3 = int(input("Introduza o terceiro número: "))

    # Encontrar maior
    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3

    # Encontrar menor
    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    print(f"\nMaior: {maior}")
    print(f"Menor: {menor}")

except ValueError:
    print("Erro: Deve introduzir números inteiros válidos.")