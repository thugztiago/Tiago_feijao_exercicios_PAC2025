j1 = input("Jogador 1: ").lower()
j2 = input("Jogador 2: ").lower()

match (j1, j2):
    case (a, b) if a == b:
        print("Empate")
    case ("pedra", "tesoura"):
        print("Jogador 1 venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")