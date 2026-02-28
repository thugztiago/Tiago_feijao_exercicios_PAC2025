requisicao = {"metodo": "POST", "conteudo": ""}

if requisicao["metodo"] == "GET":
    print("Requisição GET recebida")
elif requisicao["metodo"] == "POST" and requisicao["conteudo"]:
    print("Requisição POST com dados válidos")
elif requisicao["metodo"] == "POST":
    print("Requisição POST sem dados")
else:
    print("Método não suportado")