def ordenar_za_ignore_case(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara em minúsculas e inverte a lógica ( < )
            if lista[j].lower() < lista[j+1].lower():
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

exemplo2 = ["Python", "inteligência", "Aprender", "dados", "Rede"]
print(ordenar_za_ignore_case(exemplo2))
# Resultado: ['Rede', 'Python', 'inteligência', 'dados', 'Aprender']