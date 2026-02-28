# Receber o nome do dia
dia = input("Digite o nome do dia da semana: ").strip().lower()

# Verificar se é dia útil ou fim de semana
if dia in ["segunda", "terca", "quarta", "quinta", "sexta"]:
    print("Dia útil")
elif dia in ["sabado", "domingo"]:
    print("Fim de semana")
else:
    print("Dia inválido! Digite um dia da semana válido.")