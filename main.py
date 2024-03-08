import matplotlib.pyplot as plt
import numpy as np
import time

calculator = """
 _________________
|  _____________  |
| |_____________| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____________| |
|_________________|
    """

print(calculator)

def mostrarCalculadora(textoDeDentro: str):
    linhas = textoDeDentro.split("\n")
    padding = 2
    maximoCaracteresPorLinha = 14
    linhasCalculadora = []

    linhas = [linha.strip() for linha in linhas]
    for linha in linhas:
        if (len(linha) <= maximoCaracteresPorLinha):
            linhasCalculadora.append(linha)
            continue
        palavras = linha.split(" ")
        palavras = [palavra.strip() for palavra in palavras]
        linhaAtual = ""
        for palavra in palavras:
            if (len(linhaAtual + palavra) > maximoCaracteresPorLinha):
                linhasCalculadora.append(linhaAtual)
                linhaAtual = palavra + " "
            else:
                linhaAtual += palavra + " "
        linhasCalculadora.append(linhaAtual)

    print(" " + "_" * maximoCaracteresPorLinha + 2 * padding * "_")
    for _ in range(padding):
        print("|" + " " * maximoCaracteresPorLinha + 2 * padding * " " + "|")
    for linha in linhasCalculadora:
        print("|" + padding * " " +
              linha.center(maximoCaracteresPorLinha, " ") + padding * " " + "|")
    for _ in range(padding):
        print("|" + padding * " " + " " *
              maximoCaracteresPorLinha + padding * " " + "|")
    print("|" + "_" * maximoCaracteresPorLinha + 2 * padding * "_" + "|")

def soma(x, y):
     return x+y


def subtracao(x, y):
    return x-y

def multiplicacao(x, y):
    return x*y

def divisao(x, y):
     return x/y


def linear(x, a, b):
    return a*x+b


def plot_linear(a, b):
    
    x = np.linspace(-10,10,100)
    y = linear(x,a,b)
    plt.plot(x,y , label=f"A função linear: y={a}x+{b}")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("O Grafico de função linear")
    plt.grid(True)
    plt.show()




def exponencial(a,x):
    return a ** x


def plot_exponencial(a,b):
     x = np.linspace(-6, 6, 100)
     y = exponencial(a, x)
     plt.plot(x, y)
     plt.title(f'Gráfico da função exponencial: {a}^{b}')
     plt.xlabel('x')
     plt.ylabel('y')
     plt.grid(True)
     plt.show()



def funcao_quadratica(x, a, b, c):
    return a*x**2 +b*x+c


def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    raiz_delta = delta **0.5

    if delta < 0 :
        return "erro delta menor que zero!!"
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz
    
    raiz_positiva= -(b) + raiz_delta / (2*a)
    raiz_negativa= -(b) - raiz_delta/ (2*a)

    return raiz_positiva, raiz_negativa


def plot_quadratica(a, b, c):
    x = np.linspace(-10,10,100)
    y = funcao_quadratica(x, a, b,c)

    plt.plot(x,y,label=f"{a}x² + {b}x + {c}")
    plt.title("Gráfico de uma Função Quadrática")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def fatorial(n):
    if n < 0:
        return "Erro: Não é possivel calcular o fatorial de número negativo"
    elif n == 0:
        return 1

    resultado = 1
    for i in range(1,n+1):
         resultado *= i
    return resultado


def plot_fatorial(n):
    x = list(range(n+1))
    y = [fatorial(i) for i in x]
    plt.plot(x,y, marker='o', linestyle='-')
    plt.title('Gráfico do Fatorial')
    plt.xlabel('Número')
    plt.ylabel("Fatorial")
    plt.grid(True)
    plt.show()


def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial        
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    num1 = int(input("Digite o Primeiro Número da Soma: "))
                    num2 = int(input("Digite o Segundo Número da Soma: "))
                    print(f'O Resultado da Soma: {soma(num1,num2)}')
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    num1 = int(input("Digite o Primeiro Número da Subtração: "))
                    num2 = int(input("Digite o Segundo Número da Subtração: "))
                    print(f'O Resultado da Subtração: {subtracao(num1,num2)}')
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    num1 = int(input("Digite o Primeiro Número da Multplicação: "))
                    num2 = int(input("Digite o Segundo Número da Multplicação: "))
                    print(f'O Resultado da Multplicação: {multiplicacao(num1,num2)}')
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    num1 = int(input("Digite o Primeiro Número da Divisão: "))
                    num2 = int(input("Digite o Segundo Número da Divisão: "))
                    print(f'O Resultado da Divisão: {soma(num1,num2)}')
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    a = int(input("Digite o valor do coeficiente A: "))
                    b = int(input("Digite o valor do coeficiente B: "))
                    
                    print("Gerando o gráfico...")
                    time.sleep(2)
                    plot_exponencial(a,b)
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    a = int(input("Digite o valor do coeficiente A: "))
                    b = int(input("Digite o valor do coeficiente B: "))
                    c = int(input("Digite o valor do coeficiente C: "))
                    print("Gerando o gráfico...")
                    time.sleep(2)
                    plot_quadratica(a,b,c)
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    a = int(input("Digite o valor do coeficiente A: "))
                    b = int(input("Digite o valor do coeficiente B: "))
                    
                    print("Gerando o gráfico...")
                    time.sleep(2)
                    plot_linear(a,b)
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL f(x) = (a * x + b)")
                    num = int(input("Digite o Número do Fatorial a ser calculado: : "))
                    print("Gerando o gráfico...")
                    time.sleep(2)
                    plot_fatorial(num)
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()