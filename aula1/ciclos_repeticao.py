#while 
#for -> foreach 
#repetir ações 

#numerostring= "1"
#print(ord(numerostring))

#while True:
    #print("test")
    #para=int(input("prima1"))
    #if para == 1:
        #break   #continue
    #mais codigo 
#

lista=[1,2,3,4,5,6,7,8,9,10]

print(len(lista))

for i in range(4,1000):
    print(i)

for listaelementos in lista:
    print(listaelementos[i])

op = input("1- janeiro , 2 feveiro , 3 marco " )

match op:
    case "1":
        print("janeiro")
    case "2":
        print("feveiro")
    case "3":
        print("marco")
    case _:
        print("opcao errada")
