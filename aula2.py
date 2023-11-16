"""idade = input("qual sua idade?")
resultado = int(idade) + float(10)
print(resultado)"""

"""if 5>3:
    print("é maior que 3")
else:
    print("não é maior que 3")"""
""" A = 50
B = 40
if B>A:
    print("B maior que A")  
elif A==B:
    print("A e B são iguais")
else:
    print("foda-se tudo")
objeto = {"nome":"lucas","idade_lucas":24}
print(objeto["idade_lucas"])
paises = ()
carros = ["camaro", "ferrari", "fusca"]
#print(carros[0]) """
"""i = 1
while i <= 3:
    print(i)
    i += 1"""
    
""" i = 0
while i < 23:
    i = i + 1
    if i == 3:
        continue
    print(i) """

""" for x in carros:
    if x == "ferrari":
        break
    print(x)

for x in range(3):
    print(x)   """

def soma(n1,n2): 
    print(n1+n2)
    
def multiplicar(j1,j2):
    print(j1*j2)   

def dividir(k1,k2):
    print(k1/k2) 
   

escolha = input("[0] somar [1] multiplicação [2] divisao")
n1 = int( input("numero 1 : "))
n2 = int( input("numero 2 : "))

if escolha == "0":
    soma(n1,n2)
elif escolha == "1":
    multiplicar(n1,n2)
elif escolha == "2":
    dividir(n1,n2)
    
    






    