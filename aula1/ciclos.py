#if e match (py pv 10)

# operadores de decisao
# 
# valor1 == valor2
# valor1 != valor2 
# valor1 >= valor2
# valor1 <= valor2
# valor1 > valor2
# valor1 < valor2

val1 = 3
val2 = 2

if val1 == val2:
    print("sao iguais") # if valor1 == valor2 true
else:
    print("sao diferentes") # if valor1 == valor2 false 


if val1 > val2:
    print("o valor 1 maior que valor 2 ")
elif val1 == val2:
    print("valores iguais")
else:
    print("o val2 é maior que val1 ")


# val1 > val2  operador logico  valor2 > valor 3
# and 
# or 

val3 = 1

if val1 > val2 and val2 > val3:
    print("val1 e maior q val2 e val2 e maior que val3")

