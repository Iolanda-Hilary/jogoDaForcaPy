import  random
print("="*20, "JOGO DA FORCA", "="*20)

def leitorDePalavras():
    palavras=[] #inicia a lista vazia
    with open("animais.txt.txt", "r") as arquivo: #abre o arquivo "animais" com o termo "r" (de read), e nomeia o item como 'arquivo'
        for linha in arquivo: #para cada linha no arquivo
            linha = linha.strip() #o programa vai retirar espaços e quebras de linha
            palavras.append(linha) #e vai adicionar cada linha desse arquivo como um espaço na lista
            print(palavras)


def palavraSecreta(palavras): #recebe como argumento a lista onde estao as palavras
    numero = random.randrange(0, len(palavras))  # gera um número aleatório entre 0 e o número total de palavras na lista
    palavra_secreta = palavras[numero].upper()  # seleciona a palavra da lista pelo seu índice e a converte em letras maiúsculas
    return palavra_secreta  # retorna a palavra selecionada em letras maiúsculas