def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n


try:
    limite = int(input("Introduza um número inteiro positivo: "))
    
    if limite < 1:
        print("Deve introduzir um número positivo.")
    else:
        contador = 0
        
        for numero in range(1, limite + 1):
            if eh_perfeito(numero):
                print(f"Número perfeito encontrado: {numero}")
                contador += 1
        
        print(f"\nExistem {contador} números perfeitos entre 1 e {limite}.")

except ValueError:
    print("Erro: Deve introduzir um número inteiro válido.")