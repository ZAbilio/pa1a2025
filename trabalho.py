print("programa que compara as alturas, a media de filhos e n° de homens ")
alturas=[]
filhos=[]
alturaM=[]
totalH=0
while True:
    nome=input("\t \t Informe o seu nome: ")
    altura=int(input("\t \t Informe a sua altura (em metros): "))
    sexo=input("\t \t informe o seu sexo \n (‘m’ para masculino ou ‘f’ para feminino): ")
    filho=int(input("\t \t Informe a quantidade de filhos que você tem: "))
    alturas.append(altura)
    filhos.append(filho)
    if sexo.lower()== "f":
        alturaM.append(altura)
    else:
        totalH+=1
    stop=input("Digite 'parar' para calcular, caso contrario precione qualquer botão  ")
    if stop.lower() == 'parar':
        break
maiorAlt= max(alturas)
menorAlt= min(alturas)
if len(alturaM)>0:
    mediaM= sum(alturaM) / len(alturaM)
else:
    mediaM=0
mediaF= sum(filhos) / len(filhos)
print("\t \t Resultados")
print("\t A maior pessoa o grupo possui",maiorAlt, "\n e a menor possui", menorAlt)
print("\t A media feminina é: ", mediaM)
print("\t O numero total de homens é de: ", totalH)
print("\t A media de filhos é de: ", mediaF)