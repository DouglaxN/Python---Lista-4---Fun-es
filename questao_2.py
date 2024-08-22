def par(numero):
    if numero % 2 == 0:
        return 0
    else:
        return 1

print("Digite número 1:", end=" ")
numero1 = int(input())
print("Digite número 2:", end=" ")
numero2 = int(input())
print("Digite número 3:", end=" ")
numero3 = int(input())
print("Digite número 4:", end=" ")
numero4 = int(input())

numeros = [numero1, numero2, numero3, numero4]

soma_pares = sum(numero for numero in numeros if par(numero) == 0)

print(f"Soma dos números pares: {soma_pares}")