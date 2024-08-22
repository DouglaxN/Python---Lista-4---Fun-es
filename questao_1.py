def obter_divisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

N = int(input("Qual o valor de N? "))

print("Digite os valores:")
numeros = [int(input()) for _ in range(N)]

print("A classificação é:")
for numero in numeros:
    if eh_primo(numero):
        print(f"{numero} é primo")
    else:
        divisores = obter_divisores(numero)
        print(f"{numero} não é primo, os divisores são: {divisores}")