try:
    total_segundos = int(input("Introduza o tempo em segundos: "))
    
    if total_segundos < 0:
        print("Erro: Deve introduzir um número positivo.")
    else:
        horas = total_segundos // 3600
        resto = total_segundos % 3600
        minutos = resto // 60
        segundos = resto % 60
        
        print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")

except ValueError:
    print("Erro: Deve introduzir um número inteiro válido.")