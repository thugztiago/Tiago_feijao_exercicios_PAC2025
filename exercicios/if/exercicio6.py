try:
    nome = input("Introduza o nome do cliente: ").strip()
    compra = float(input("Introduza o valor da compra (€): "))

    if compra < 0:
        print("Erro: O valor da compra deve ser positivo.")
    else:
        # Calcular desconto
        if compra <= 200:
            desconto = compra * 0.10
        elif compra <= 500:
            desconto = compra * 0.15
        else:
            desconto = compra * 0.20

        total = compra - desconto

        # Mostrar resultado
        print(f"\nNome: {nome}")
        print(f"Compra: {compra:.2f}€")
        print(f"Desconto: {desconto:.2f}€")
        print(f"Total a pagar: {total:.2f}€")

except ValueError:
    print("Erro: Deve introduzir um valor numérico válido.")