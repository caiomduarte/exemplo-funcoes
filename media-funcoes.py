import os 

# Importando as funcoes do arquivo funcoes.py
import funcoes

os.system("cls")

funcoes.exibir_titulo("Calculando a Média com funções")


nome = input("Digite o nome do Aluno: ")
turma = input("Informe sua turma: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

funcoes.calcular_media(nome,turma,nota1,nota2,nota3)

resultadoFinal = funcoes.calcularMediaComRetorno(nota1,nota2,nota3)

funcoes.verificar_situacao_do_aluno()

input("Pressione <Enter> para continuar..")