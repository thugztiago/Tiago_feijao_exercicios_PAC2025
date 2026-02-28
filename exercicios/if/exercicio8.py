# Lista para armazenar as notas
notas = []

# Ler as notas dos 10 alunos
for i in range(1, 11):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i} (0 a 20): "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Deve ser entre 0 e 20.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

# Calcular a média
media = sum(notas) / len(notas)

# Contar alunos com nota igual ou acima da média
acima_media = sum(1 for nota in notas if nota >= media)

# Mostrar resultados
print(f"\nMédia das notas: {media:.2f}")
print(f"Número de alunos com nota igual ou acima da média: {acima_media}")