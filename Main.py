from Func import *

print('''
░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ███████╗░█████╗░██████╗░░█████╗░░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║███████║  █████╗░░██║░░██║██████╔╝██║░░╚═╝███████║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══██║  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░██║  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝''')

leitor = leitorDePalavras().strip()
acertou = acertadas(leitor)

perdeu = False
ganhou = False
erros = 0


print(acertou)
letrasFaltando=len(acertou)

print("faltam {} letras a acertar".format(letrasFaltando))

while not perdeu and not ganhou:
    resp = resposta()
    if resp in leitor:
        acerto(resp, acertou, leitor)
        letrasFaltando = str(acertou.count('_'))
        if (letrasFaltando == "0"):
            print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(leitor).upper())
        else:
                erros += 1
                print(acertou)
                print('Ainda faltam acertar {} letras'.format(letrasFaltando))
                print('Você ainda tem {} tentativas'.format(10-erros))
                forca(erros)

    perdeu = erros == 10
    ganhou = "_" not in acertou
    print(acertou)
    tudo=print("você já sabe a palavra?")
