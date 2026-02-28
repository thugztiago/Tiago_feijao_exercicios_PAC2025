operacao = input("Operação (soma, subtrai, multiplica, divide): ").lower()
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

if operacao == "soma":
    print(num1 + num2)
elif operacao == "subtrai":
    print(num1 - num2)
elif operacao == "multiplica":
    print(num1 * num2)
elif operacao == "divide":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")