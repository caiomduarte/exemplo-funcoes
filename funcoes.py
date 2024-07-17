# Declarando a função
def calcular_media(nomeAluno, turmaAluno, nota1, nota2, nota3):
    global media
    media = (nota1 + nota2 + nota3) / 3
    print("Olá", nomeAluno, "da turma:" , turmaAluno, " Sua Media foi: ", media)

def calcularMediaComRetorno(nota1, nota2, nota3):
    global media
    media = (nota1 + nota2 + nota3) / 3
    return media


def verificar_situacao_do_aluno():
    if(media >=5):
        print("Parabéns, você foi aprovado!")
    elif(media >=3 and media<=4):
        print("Você ficou de recuperação")
    else:
        print("Você foi reprovado")

def exibir_titulo(tituloDoPrograma):
    print(tituloDoPrograma)        