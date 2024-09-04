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
    primeiro, segundo = 0, 1
    seq=[]
    print("Verifique se o número faz parte da sequencia de fibonacci")
    for _ in range(a):
        seq.append(primeiro)
        print(primeiro, end=" \n")
        resultado = primeiro + segundo
        primeiro = segundo
        segundo = resultado
    Num1 = int(input("\nDigite um número\n"))
    if Num1 in seq:
        print(f"o número {Num1} pertence a sequencia de fibonacci")
    else:
        print(f"o número {Num1} não pertence a sequencia de fibonacci")
    

def Questao3():
    with open("dados.json","r")as file:
        dados = json.load(file)
    valores = [item["valor"] for item in dados if item["valor"] > 0]
    fatu_min = min(valores)
    fatu_max = max(valores)
    media_fatu = sum(valores) / len(valores)
    superior_media = sum(1 for valor in valores if valor > media_fatu)

    print("O menor faturamento diario foi:", fatu_min)
    print("O maior faturamento diario foi:", fatu_max)
    print("Os dia que o Faturamento diario passou a media mensal", superior_media)


def Questao4():
    fatu = [67836.43, 36678.66, 29229.48, 27165.48, 19849.53]
    total = sum(fatu)
    porcetagem = [(valor / total) * 100 for valor in fatu]

    print(f"O valor de todos os faturamento e R${total}")
    estado = ["SP", "RJ", "MG","ES","Outros"]
    for est, fatuporcetagem in zip(estado,porcetagem):
        print(est,fatuporcetagem,"%")


def Questao5():
   palavra = str(input("Escreva qualquer palavra\n"))
   inversor = palavra[::-1]
   print(inversor)

Questao4()