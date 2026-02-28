for i in range(256):
    print(f"Codigo: {i:3} -> Caractere: {chr(i)}")
    
    # A cada 20 linhas, perguntar se deseja continuar
    if (i + 1) % 20 == 0:
        opcao = input("\nDeseja continuar? (s/n): ").strip().lower()
        if opcao == 'n':
            print("Programa terminado.")
            break