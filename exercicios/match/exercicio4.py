valor = [10, 20, 30]  # Pode alterar aqui o valor para testar

if isinstance(valor, int):
    print("Número inteiro")
elif isinstance(valor, float):
    print("Número decimal")
elif isinstance(valor, str):
    if valor.replace('.', '', 1).isdigit():
        print("String numérica")
    else:
        print("String textual")
elif isinstance(valor, list):
    print("Lista")
else:
    print("Tipo desconhecido")