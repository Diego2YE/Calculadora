def adicionar(numeros):
    return sum(numeros)
def subtrair(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado
def multiplicar(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado
def dividir(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        if num == 0:
            return "ERRO: Divisão por zero"
        resultado /= num
    return resultado
def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1 - adição (+)")
    print("2 - subtração (-)")
    print("3 - multiplicação (*)")
    print("4 - divisão (/)")
def obter_numeros():
    numeros = []
    print("Digite de 2 até 10 números (digite 'f' para parar antes):")
    while len(numeros) < 10:
        entrada = input(f'Digite o {len(numeros)+1}º número: ')
        if entrada.lower() == "f":
            if len(numeros) >= 2:
                break
            else:
                print('Você precisa digitar pelo menos 2 números.')
                continue
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print('ERRO: Digite um número ou "f"')
    return numeros
calculadora()
escolha = input('Escolha a operação (1/2/3/4): ')
numeros = obter_numeros()
if escolha == "1":
    resultado = adicionar(numeros)
elif escolha == "2":
    resultado = subtrair(numeros)
elif escolha == "3":
    resultado = multiplicar(numeros)
elif escolha == "4":
    resultado = dividir(numeros)
else:
    resultado = "Operação Inválida"
print(f"Resultado: {resultado}")
