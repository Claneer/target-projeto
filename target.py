def Questao1():
    indice=13
    soma=0
    k=0
    while k < indice:
        soma+=k
        print(soma)
        k+=1
#A variavel "soma" chega ate 78

def Questao2(a):
    #para executar essa questão defina a variavel "A"
    x, y=0, 1
    seq=[]
    print("Verifique se o número faz parte da sequencia de fibonacci")
    for _ in range(a):
        seq.append(x)
        print(x,end=" \n")
        b=x+y
        x=y
        y=b
    z=int(input("\nDigite um número\n"))
    if z in seq:
        print(f"o número {z} pertence a sequencia de fibonacci")
    else:
        print(f"o número {z} não pertence a sequencia de fibonacci")
    
def Questao3():
    fatu = [1660, 2000, 1500, 4605, 2077, 0, 0, 4056, 3500, 0, 0, 5743, 4733, 0, 0, 6503, 5275, 0, 0, 7624, 6500, 0, 0, 8000, 7840, 0, 0, 9000, 10000, 0, 0]
    fatu = [f for f in fatu if f > 0]
    x = min(fatu)
    y = max(fatu)
    mm = sum(fatu) / len(fatu)
    z = sum(1 for f in fatu if f > mm)

    print("O menor faturamento diario foi:",x)
    print("O maior faturamento diario foi:",y)
    print("Os dia que o Faturamento diario passou a media mensal",z)

def Questao4():
    fatu = [67836.43, 36678.66, 29229.48, 27165.48, 19849.53]
    x = sum(fatu)
    y = [(valor/x)*100 for valor in fatu]

    print(f"O valor de todos os faturamento e R${x}")
    print(f"Em ordem(SP,RJ,MG,ES,OUTROS){y}%")

def Questao5():
   x=str(input("Escreva qualquer palavra"))
   y=x[::-1]
   print(y)

Questao5()