salarioAt=float(input("informe o salario atual:"))
perc=int(input("percentual e reajuste:"))
perc2=perc/100
aumento=perc2*salarioAt
novoS=aumento+salarioAt
print("o salario era:",salarioAt,"\n teve um aumento de:",aumento,"\n ficando com um valor de:",novoS)