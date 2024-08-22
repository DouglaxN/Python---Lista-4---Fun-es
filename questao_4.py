def inverter_numero(numero):
    numero_str = str(numero)
    if numero_str[0] == '_':
        return '-' + numero_str[:0:-1]
    else:
        return numero_str[::-1]
    
valor = int(input("Digite um valor: "))

inverso = inverter_numero(valor)
print(f"Inverso: {inverso}")