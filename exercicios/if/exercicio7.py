try:
    nota1 = float(input("Introduza a primeira nota (peso 2): "))
    nota2 = float(input("Introduza a segunda nota (peso 3): "))
    nota3 = float(input("Introduza a terceira nota (peso 5): "))

    # Validar notas
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        print("Erro: As notas devem estar entre 0 e 10.")
    else:
        # Calcular média ponderada
        media = (nota1*2 + nota2*3 + nota3*5) / (2 + 3 + 5)

        # Mostrar resultado
        print(f"\nMédia: {media:.1f}")
        if media >= 6:
            print("Aprovado")
        else:
            print("Reprovado")

except ValueError:
    print("Erro: Deve introduzir valores numéricos válidos.")