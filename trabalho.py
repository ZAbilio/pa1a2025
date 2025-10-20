print("programa que compara as alturas, a media de filhos e n° de homens ")
nome=[]
altura=[]
sexo=[]
while True:
    nome=input("\t \t Informe o seu nome: ")
    altura=float(input("\t \tInforme a sua altura atual: "))
    sexo=input("\t \t informe o seu sexo \n (‘m’ para masculino ou ‘f’ para feminino): \n")
    filho=input("\t \t Informe a quantidade de filhos que você tem: ")
    stop=input("Digite 'parar' para encerrar e fazer os calculos ")
    if stop.lower() == 'parar':
        break

print(nome, altura, sexo,filho )