def comparar_palavras(p1, p2):
    # Retorna True se p1 > p2 (deve trocar)
    len1, len2 = len(p1), len(p2)
    for i in range(min(len1, len2)):
        if ord(p1[i]) > ord(p2[i]):
            return True
        elif ord(p1[i]) < ord(p2[i]):
            return False
    return len1 > len2 # Caso uma seja prefixo da outra

def ordenar_az(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_palavras(lista[j], lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

palavras = ["banana", "uva", "abacaxi", "laranja"]
print(ordenar_az(palavras)) 
# Resultado: ['abacaxi', 'banana', 'laranja', 'uva']