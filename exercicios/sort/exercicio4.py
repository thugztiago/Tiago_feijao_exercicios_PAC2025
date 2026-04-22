def contar_minusculas(palavra):
    contagem = 0
    for char in palavra:
        if 'a' <= char <= 'z': # Ou: if 97 <= ord(char) <= 122:
            contagem += 1
    return contagem

def ordenar_por_peso_minusculas(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contar_minusculas(lista[j]) > contar_minusculas(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

exemplo4 = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
print(ordenar_por_peso_minusculas(exemplo4))
# Resultado: ['CÓDIGO', 'intELIGENTE', 'PYthon', 'dados', 'banana']