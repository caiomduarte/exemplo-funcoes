
import os


os.system("cls")



valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print("Operações: \n 1 - SOMAR \n 2 - SUBTRAIR \n 3 - Multiplicar \n 4 - Dividir")
operacao = int(input("Digite a operação desejada: "))


resultado=0
# Criando as funções

def exibir_resultado(resultado):
     print("O Resultado: ", resultado)


def somar_valores(valor1, valor2):
    
    resultado = valor1 + valor2
    exibir_resultado(resultado)     

def subtrair_valores(valor1, valor2):
     global resultado
     resultado = valor1 - valor2
     exibir_resultado() 

def multiplicar_valores(valor1, valor2):
     global resultado
     resultado = valor1 * valor2
     exibir_resultado()

def dividir_valores(valor1, valor2):
     global resultado
     resultado = valor1 / valor2
     exibir_resultado()       



# Verificando a operacao escolhida
if(operacao == 1):
    somar_valores(valor1,valor2)
  
elif(operacao == 2):
    subtrair_valores(valor1,valor2)

elif(operacao == 3):
     multiplicar_valores(valor1,valor2)

elif(operacao == 4):
     dividir_valores(valor1,valor2)

input("Pressione <ENTER> para continuar...")



