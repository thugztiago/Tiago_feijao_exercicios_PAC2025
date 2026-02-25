quantidade = 0
numero = 2  # primeiro número primo

while quantidade < 10:
    primo = True
    
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(numero)
        quantidade += 1
    
    numero += 1