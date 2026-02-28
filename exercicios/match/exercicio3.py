pedido = {"tipo": "venda", "valor": 250}

if pedido["tipo"] == "compra":
    print(f"Compra de {pedido['valor']}€")
elif pedido["tipo"] == "venda":
    print(f"Venda de {pedido['valor']}€")
else:
    print("Pedido desconhecido")