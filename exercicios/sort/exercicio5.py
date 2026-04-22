palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

# --- ETAPA 1: Agrupamento ---
grupos = {}

for p in palavras:
    inicial = p[0].lower()
    if inicial not in grupos:
        grupos[inicial] = []
    grupos[inicial].append(p)

# --- ETAPA 2 e 3: Ordenação Manual (Bubble Sort) ---
for letra in grupos:
    lista_do_grupo = grupos[letra]
    n = len(lista_do_grupo)
    
    # Algoritmo de ordenação manual
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos as palavras caractere a caractere usando ord()
            palavra1 = lista_do_grupo[j]
            palavra2 = lista_do_grupo[j + 1]
            
            # Se a palavra1 for alfabeticamente maior que a palavra2, trocamos
            if palavra1 > palavra2: 
                lista_do_grupo[j], lista_do_grupo[j + 1] = lista_do_grupo[j + 1], lista_do_grupo[j]

# Resultado final
import pprint
pprint.pprint(grupos)