numero = int(input("Digite um número inteiro: "))

soma_total = 0
subtracao_total = 0
multiplicacao_total = 1
divisao_total = 1  # iniciamos com 1 para multiplicar/dividir

contador_operacoes = 0

for i in range(1, numero):
    # Soma
    soma_total += numero + i
    contador_operacoes += 1

    # Subtração
    subtracao_total += numero - i
    contador_operacoes += 1

    # Multiplicação
    multiplicacao_total *= numero * i
    contador_operacoes += 1

    # Divisão
    divisao_total /= i  # dividindo pelo número menor
    contador_operacoes += 1

print(f"Soma total: {soma_total}")
print(f"Subtração total: {subtracao_total}")
print(f"Multiplicação total: {multiplicacao_total}")
print(f"Divisão total: {divisao_total}")
print(f"Total de operações efetuadas: {contador_operacoes}")