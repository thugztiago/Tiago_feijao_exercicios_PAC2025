# Série de Fibonacci - primeiros 60 números

a = 1
b = 1

print(a)
print(b)

for i in range(58):  # já temos os 2 primeiros
    proximo = a + b
    print(proximo)
    a = b
    b = proximo