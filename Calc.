def adicionar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return 'ERRO: Divisão por zero'
def calculadora():
    print("Calculadora Simples")
    print('Operações disponiveis')
    print('1 - adição (+)')
    print('2 - subtração (-)')
    print('3 - multiplicação (*)')
    print('4 - divisão (/)')
calculadora()
escolha = input('Escolha a operação (1/2/3/4): ')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if escolha == '1':
    resultado = adicionar(n1,n2)
elif escolha == '2':
    resultado = subtrair(n1,n2)
elif escolha == '3':
    resultado = multiplicar(n1,n2)
elif escolha == '4':
    resultado = dividir(n1,n2)
else:
    resultado = 'Operação Invalida'
print(f'Resultado: {resultado}')
