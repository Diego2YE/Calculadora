def calculadora():
    print("Calculadora")
    print("Você pode digitar uma expressão com até 10 números usando +, -, * e /")
    print("Exemplo: 2 + 3 * 4 - 5 / 2")
def obter_expressao():
    while True:
        expr = input("Digite a expressão: ")
        numeros = [s for s in expr.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split() if s.strip()]
        if len(numeros) > 10:
            print("ERRO: Você pode usar no máximo 10 números.")
            continue
        try:
            for n in numeros:
                float(n)
            return expr
        except ValueError:
            print("ERRO: Expressão inválida. Digite apenas números e operadores + - * /.")
def calcular(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except ZeroDivisionError:
        return "ERRO: Divisão por zero"
    except:
        return "ERRO: Expressão inválida"
calculadora()
expressao = obter_expressao()
resultado = calcular(expressao)
print(f"Resultado: {resultado}")
