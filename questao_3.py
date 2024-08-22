#Faça um programa para imprimir:

#1
#2   2
#3   3   3
#.....
#n   n   n   n   n   n  ... n
#para um n informado pelo usuário.

#Use uma função que receba um valor n inteiro como parâmetro e imprima até a n-ésima linha.

#OBS.: Não se esqueça de verificar se o número N recebido é positivo não nulo. Talvez você possa criar uma função pra isso também. ;-)

def validar_n(n):
    return n > 0

def imprimir_padrao(n):
    for i in range(1, n + 1):
        print(' '.join([str(i)] * i))

n = int(input("Digite o valor de n: "))

if validar_n(n):
    imprimir_padrao(n)

else:
    print("Valor inválido!")