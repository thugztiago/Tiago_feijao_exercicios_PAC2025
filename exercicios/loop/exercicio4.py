numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("Não é número primo")
else:
    primo = True
    
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print("É número primo")
    else:
        print("Não é número primo")