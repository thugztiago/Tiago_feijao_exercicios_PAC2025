try:
    saldo = float(input("Introduza o saldo inicial: "))
    cheque = float(input("Introduza o valor do cheque: "))

    if cheque <= 0:
        print("Erro: O valor do cheque deve ser positivo.")
    elif cheque > saldo:
        print("Cheque não pode ser descontado. Saldo insuficiente.")
    else:
        saldo -= cheque
        print(f"Cheque descontado, saldo atualizado: {saldo:.2f}")

except ValueError:
    print("Erro: Deve introduzir valores numéricos válidos.")