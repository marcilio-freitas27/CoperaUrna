# Projeto CoperaUrna

from time import sleep
zerésima = "\033[34;1mNENHUM VOTO COMPUTADO!\033[m"
print('\033[36mImprimindo a zerésima. Aguarde...\033[m')
sleep(5)
print(zerésima)

print('''Candidatos:\n\nNulo = 0;\nCandidato1 = 1;\nCandidato2 = 2;\nCandidato3 = 3;\nBranco = quaquer outro numero\n''')

# Escolha do voto
print('''Candidatos:\n\nNulo = 0;\n@Marcílio = 1;\n@Júnior = 2;\n@Pedro = 3;\nBranco = quaquer outro numero\n''')

branco = 0
nulo = 0
can1 = 0
can2 = 0
can3 = 0

# Condição para escolha do candidato
eleitor = 1
while eleitor <= 5:
    # definindo variável como global para ser enxergada dentro da identação
    globals = (branco, nulo, can1, can2, can3)

    voto = int(input("Digite o número do seu candidato: "))
    if voto == 0:
        print('Você votou nulo.')
        nulo +=1
    elif voto == 1:
        print('Você votou no candidato1.')
        can1 += 1
    elif voto == 2:
        print('Você votou no candidato2.')
        can2 += 1
    elif voto == 3:
        print('Você votou no candidato3.')
        can3 += 1
    else:
        print('Você votou em branco.')
        branco +=1
    eleitor += 1

print('Candidato1: ',can1,'\nCandidato2: ',can2,'\nCandidato3: ',can3,'\nNulo: ',nulo,'\nBranco: ',branco,"\n")

# resultado da votação

if can2 > can1 and can3 < can2 and nulo < can2 and branco < can2:
    print("\033[38mFim da eleição, o vencedor foi o Candidato2")
elif can3 > can1 and can2 < can3 and nulo < can3 and branco < can3:
    print("Fim da eleição, o vencedor foi o Candidato3")
elif can1 > can2 and can3 < can1 and nulo < can1 and branco < can1:
    print("Fim da eleição, o vencedor foi o Candidato1")
elif nulo > can1 and can3 < nulo and can2 < nulo and branco < nulo:
    print("Fim da eleição, o vencedor foi o Nulo")
else:
    print("Fim da eleição, o vencedor foi o Branco")