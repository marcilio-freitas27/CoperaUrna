
from time import sleep

zerésima = "\033[34;1mNENHUM VOTO COMPUTADO!\033[m"
print('\033[36mImprimindo a zerésima. Aguarde...\033[m')

# contagem antes da votação
sleep(5)
print(zerésima)

print('''Lista de Candidatos:\n\nNulo = 0;\nCandidato1 = 1;\nCandidato2 = 2;\nCandidato3 = 3;\nBranco = qualquer outro numero/caractere\n''')

branco = 0
nulo = 0
can1 = 0
can2 = 0
can3 = 0

# senha de confirmação
sua_senha = input('Escolha sua senha: ')

# Condição para escolha do candidato
eleitor = 's'
empate = 'n'
votacao = 0
while eleitor == 's'.lower() or empate == 's'.lower():
    while votacao < 5:
        voto = input("Digite o número do seu candidato: ")
        if voto == '0':
            #Você votou nulo
            nulo +=1
        elif voto == '1':
            #Você votou no candidato1.
            can1 += 1
        elif voto == '2':
            #Você votou no candidato2.
            can2 += 1
        elif voto == '3':
            #Você votou no candidato3.
            can3 += 1
        else:
            #Você votou em branco.
            branco +=1
        votacao += 1
    eleitor = 'n'
    
    # imprime o resultado
    while True:
        senha = input('Digite a senha para finalizar: ')
        if senha != sua_senha:
            print("Senha invalida. Tente novamente.")
        else:
            print('Eleitores: ',votacao,'\nCandidato1: ',can1,'\nCandidato2: ',can2,'\nCandidato3: ',can3,'\nNulo: ',nulo,'\nBranco: ',branco,"\n")
            break

    # resultado da votação

    if can2 > can1 and can3 < can2:
        print(f"Fim da eleição, o vencedor foi o Candidato2 com {can2} votos")
        empate = 'n'
    elif can3 > can1 and can2 < can3:
        print(f"Fim da eleição, o vencedor foi o Candidato3 com {can3} votos")
        empate = 'n'
    elif can1 > can2 and can3 < can1:
        print(f"Fim da eleição, o vencedor foi o Candidato1 com {can1} votos")
        empate = 'n'

    # empate

    elif can1 == can2:
        print("Houve empate! Preparem-se para o 2º turno!")
        empate = 's'
    elif can3 == can1 :
        print("Houve empate! Preparem-se para o 2º turno!")
        empate = 's'
    elif can3 == can2:
        print("Houve empate! Preparem-se para o 2º turno!")
        empate = 's'

    # reseta todos os votos para fazer o desempate
    branco = 0
    nulo = 0
    can1 = 0
    can2 = 0
    can3 = 0
    votacao = 0
    