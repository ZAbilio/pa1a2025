'''print("calculadora em Python")
while  True:
   vl1=float(input("informe o primeiro valor: "))
   vl2=float(input("informe o segundo valor: ")) 
   sinal=input("informe o tipo de conta que deseja realizar'+,-,x,/': ")
   match sinal:
      case "+":
         resultado=vl1+vl2
         print("seu resultado é: ",resultado) 
      case "-":
         resultado=vl1-vl2
         print("seu resultado é: ",resultado)
      case "x":
           resultado=vl1*vl2
           print("seu resultado é: ",resultado)
      case "/":
           resultado=vl1/vl2
           print("seu resultado é: ",resultado) 
      case _:
           print("tipo invalido")
i=input("digite (s/n) para um novo calculo.") 
while False:

       print("programa encerrado")'''
''' print("\n 1-soma \n 2-subtração \n 3-multiplicação \n 4-divisão")'''


'''print("calculadora de media ")
nm1=float(input("informe o valor 1: "))
nm2=float(input("informe o valor 2: "))
nm3=float(input("informe o valor 3: "))'''
'''def saudar():
   print(" ola mundo")
saudar()'''
'''def soma(a,b):
   return a+b
v1=float(input("fale o valor 1: "))
v2=float(input("fale o valor 2: "))
resultado= soma(v1, v2)
print(v1,"+", v2,"=",resultado)'''
def media(v1,v2, v3, v4):
   md=v1+v2+v3+v4/4
n1=float(input("informe o valor 1: "))
n2=float(input("informe o valor 2: "))
n3=float(input("informe o valor 3: "))
n4=float(input("informe o valor 4: "))
media(n1, n2, n3, n4)

