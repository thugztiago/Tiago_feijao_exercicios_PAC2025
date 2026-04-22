frase = input("Introduza uma frase: ")
palavras = frase.split()
contagem = {}

for p in palavras:
    contagem[p] = contagem.get(p, 0) + 1

print(contagem)