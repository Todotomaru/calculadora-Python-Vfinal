import matplotlib.pyplot as plt
import numpy as np

def som(a , b):
    soma = a + b
    return soma
def sub(a , b):
    subtração = a - b
    return subtração
def multi(a, b):
    multiplicação = a * b
    return multiplicação
def div(a, b):
    divisão = a / b
    return divisão
def pot(a, b):
    potenciação = a ** b
    return potenciação
def fat(a:int) -> int:
    if a > 0:
        fatorial = 1
        for i in range(1, a+1):
            fatorial *= i
        return fatorial
    elif a < 0:
        print("erro: comando invalido")
    else:
        return 1
def plotfat(a):
    x = list(range(a + 1))
    y = [fat(i) for i in x]
    plt.plot(x, y, marker ='o', linestyle= '-')
    plt.title('grafico de fatorial')
    plt.xlabel('número')
    plt.ylabel('fatorial')
    plt.grid(True)
    plt.show()
def plotpot(a, b):
    x = np.linspace(0, 10, 100) 
    y = pot(a, x)
    plt.plot(x, y)
    plt.title(f'grafico exponencial {a}**{b}')
    plt.xlabel('expoente')
    plt.ylabel('número')
    plt.grid(True)
    plt.show()
def plotlin(x, a, b):
    x = np.linspace(-10, 10, 100)
    y = linear(x, a, b)
    plt.plot(x, y)
    plt.title('grafico linear')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
def funseg(a, b, c):
    if a == 0:
        print("Raiz invalida")
    if a != 0:
        delta = ((b**2) - (4 * a * c))
        raiz1 = (((-b) + (delta ** 1/2)) / (a*2))
        raiz2 = (((-b) - (delta ** 1/2)) / (a*2))
        return raiz1, raiz2
def linear(x, a, b):
    return ((a*x) + b)
    
print("----------Bem vindo à Calculadora Python----------")
print("Gostaria de realizar um cálculo?\n s/n")
n1 = input()

while n1 == "s" :
    print("Gostaria de realizar o que?")
    print("----------------------------------")
    print(" 1 - soma\n 2 - subtração\n 3 - divisão\n 4 - multiplicação\n 5 - potenciação\n 6 - fatoração\n 7 - função de 2° grau\n 8 - função linear")
    print("----------------------------------")
    n2 = int(input("escolha a operação: "))
    print("----------------------------------")
    if n2 <= 0 or n2 > 8 :
        print("ERRO (insira um comando válido: 1-8)")
        break
    print("Insira os números os números:")
    if n2 < 5 :
        a = float(input("Insira o número 1: "))
        b = float(input("Insira o número 2: "))
        if n2 == 1 :
            print("calculando.")
            print("calculando..")
            print("calculando...")
            resposta1 = som(a , b)
            print(f"Adição: {a} + {b} = {resposta1}")
        elif n2 == 2 :
            print("calculando.")
            print("calculando..")
            print("calculando...")
            resposta2 = sub(a , b)
            print(f"Subtração: {a} - {b} = {resposta2}")
        elif n2 == 3 :
            print("calculando.")
            print("calculando..")
            print("calculando...")
            resposta3 = multi(a , b)
            print(f"Multiplicação: {a} * {b} = {resposta3}")
        elif n2 == 4 :
            print("calculando.")
            print("calculando..")
            print("calculando...")
            resposta4 = div(a , b)
            print(f"Divisão: {a} / {b} = {resposta4}")
    elif n2 == 5 :
        a = int(input("Insira o número 1: "))
        b = int(input("Insira o número 2: "))
        print("calculando.")
        print("calculando..")
        print("calculando...")
        resposta5 = pot(a , b)
        resposta5_1= plotpot(a, b)
        print(f"Potenciação: {a} ** {b} = {resposta5}")
    elif n2 == 6 :
        a = int(input("Insira o número 1: "))
        print("calculando.")
        print("calculando..")
        print("calculando...")
        resposta6 = fat(a)
        resposta6_1 = plotfat(a)
        print(f"Fatoração: {a} fatorado = {resposta6}")
    elif n2 == 7 :
        a = float(input("Insira o número 1: "))
        b = float(input("Insira o número 2: "))
        c = float(input("Insira o número 3: "))
        print("calculando.")
        print("calculando..")
        print("calculando...")
        resposta7 = funseg(a, b, c)
        print(f"A resposta pra função de segundo grau é {resposta7}.")
    elif n2 == 8 :
        print("calculando.")
        print("calculando..")
        print("calculando...")
        x = float(input("Insira o número x: "))
        a = float(input("Insira o número a: "))
        b = float(input("Insira o número b: "))
        resposta8 = linear(x, a, b)
        resposta8_1 = plotlin(x, a, b)
        print(f"O resultado da função linear é {resposta8}.")
        

    print("Deseja continuar? s/n")
    n1 = input()

if n1 == "n" :
    encerramento = """
  ´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´

    Obrigado por usar essa mizera.
    """
    print (encerramento)
else:
    print("ERRO")