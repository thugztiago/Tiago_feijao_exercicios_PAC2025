contador = 0
soma = 0

while contador < 30:
    try:
        numero = int(input(f"Introduza o {contador+1}º número par (1-50): "))
        
        # Validação do intervalo
        if numero < 1 or numero > 50:
            print("Erro: O número deve estar entre 1 e 50.")
            continue
        
        # Validação se é par
        if numero % 2 != 0:
            print("Erro: O número deve ser par.")
            continue
        
        soma += numero
        contador += 1

    except ValueError:
        print("Erro: Deve introduzir um número inteiro válido.")

media = soma / 30
print(f"\nA média dos 30 números pares é: {media}")