produto = {"categoria": "eletrônico", "preco": 1500}

if produto["categoria"] == "eletrônico" and produto["preco"] > 1000:
    print("Produto de luxo")
elif produto["categoria"] == "eletrônico":
    print("Produto comum")
elif produto["categoria"] == "alimento":
    print("Produto alimentar")
else:
    print("Categoria desconhecida")