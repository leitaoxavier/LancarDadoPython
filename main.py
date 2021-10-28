"""
Jogo dos dados
"""
from time import sleep
import random

print("---------JOGO DOS DADO-----------")
print()

print("Deseja lançar o dado?")
print("s/n ?")
resposta = input()
if resposta.upper():
    resposta = resposta.lower()

while resposta != 's' and resposta != 'n':
    print("Resposta inválida!\n")
    print("Digite apenas s para sim ou n para não!")
    print()
    print("Deseja lançar o dado?")
    print("s/n ?")
    resposta = input()
    if resposta.upper():
        resposta = resposta.lower()

while resposta == 's':
    print("Número sorteado do dado foi:", random.randint(1, 7))
    print("\nDeseja lançar o dado novamente?")
    print("s/n ?")
    resposta = input()
    if resposta.upper():
        resposta = resposta.lower()

if resposta == 'n':
    print("O programa vai fechar em: ")
    sleep(1)
    for cont in range(5, -1, -1):
        print(cont)
        sleep(1)
        if cont == 1:
            exit()



