mensagem = input("Digite a mensagem: ").lower()

if mensagem in ["olá", "bom dia"]:
    print("Saudação")
elif mensagem.endswith("?"):
    print("Pergunta")
elif "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")
else:
    print("Mensagem genérica")