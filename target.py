import json
def Questao1():
    indice = 13
    soma = 0
    k = 0
    while k < indice:
        soma += k
        print(soma)
        k += 1
#A variavel "soma" chega ate 78


def Questao2(a):
    #para executar essa questão defina a variavel "A"
    x, y = 0, 1
    seq=[]
    print("Verifique se o número faz parte da sequencia de fibonacci")
    for _ in range(a):
        seq.append(x)
        print(x, end=" \n")
        b = x + y
        x = y
        y = b
    z = int(input("\nDigite um número\n"))
    if z in seq:
        print(f"o número {z} pertence a sequencia de fibonacci")
    else:
        print(f"o número {z} não pertence a sequencia de fibonacci")
    

def Questao3():
    with open("dados.json","r")as file:
        dados = json.load(file)
    valores = [item["valor"] for item in dados if item["valor"] > 0]
    x = min(valores)
    y = max(valores)
    mm = sum(valores) / len(valores)
    z = sum(1 for valor in valores if valor > mm)

    print("O menor faturamento diario foi:", x)
    print("O maior faturamento diario foi:", y)
    print("Os dia que o Faturamento diario passou a media mensal", z)


def Questao4():
    fatu = [67836.43, 36678.66, 29229.48, 27165.48, 19849.53]
    x = sum(fatu)
    y = [(valor / x) * 100 for valor in fatu]

    print(f"O valor de todos os faturamento e R${x}")
    estado = ["SP", "RJ", "MG","ES","Outros"]
    for est, fatuporcetagem in zip(estado,y):
        print(est,fatuporcetagem)


def Questao5():
   x = str(input("Escreva qualquer palavra\n"))
   y = x[::-1]
   print(y)

if __name__ == "__main__":
    pass
    estados = ["DF", "SP", "MG"]
    parcial = [1, 2, 3]

    for est, par in zip(estados, parcial):
        print(est, par)