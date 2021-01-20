from time import sleep

zerésima = "\033[34;1mNENHUM VOTO COMPUTADO!\033[m"
print('\033[36mImprimindo a zerésima. Aguarde...\033[m')

# contagem antes da votação
sleep(5)
print(zerésima)
# lista dos candidatos empatados
numeros = []

print('''Lista de Candidatos:\n\nNulo = 0;\nCandidato1 = 1;\nCandidato2 = 2;
\nCandidato3 = 3;\nBranco = qualquer outro numero/caractere\n''')

#candidatos
candidatos = [0,0,0,0,0]

# senha de confirmação
sua_senha = input('Escolha sua senha: ')
while True:
    if sua_senha == '':
        print("A senha não pode ser vazia. Tente novamente.")
        sua_senha = input('Escolha sua senha: ')
    else:
        break

# Condição para escolha do candidato
eleitores = 5
eleitor = 's'
empate = 'n'
votacao = 0
while eleitor == 's'.lower() or empate == 's'.lower():
    while votacao < 5 and empate == 'n':
        voto = input("Digite o número do seu candidato: ")
        
        # alterar voto
        resp = input('Deseja corrigir o voto? ')

        if resp in 'Ss':
            voto = input("Informe o novo voto: ")
            print('Voto corrigido.')

        if voto == '0':
            #Você votou nulo 
            candidatos[3] += 1
        elif voto == '1':
            #Você votou no candidato1.
            candidatos[0] += 1
        elif voto == '2':
            #Você votou no candidato2.
            candidatos[1] += 1
        elif voto == '3':
            #Você votou no candidato3.
            candidatos[2] += 1
        elif voto == '':
            #Você votou em branco.
            candidatos[4] += 1
        else:
            print('Escolha o candidato correto.')
            votacao -=1

        votacao += 1
    eleitor = 'n'

    # restrição para o desempate
    # votos apenas para os empatados
    while votacao < 5 and empate == 's':
        voto = input("Digite o número do seu candidato: ")
        resp = input('Deseja corrigir o voto? ')

        if resp in 'Ss':
            voto = input("Informe o novo voto: ")
            print('Voto corrigido.')

        #só poderão ser escolhidos os candidatos na lista de empate
        if voto in numeros:
            if voto == '1':
                candidatos[0] += 1
                votacao += 1
            elif voto == '2':
                candidatos[1] += 1
                votacao += 1
            elif voto == '3':
                candidatos[2] += 1
                votacao += 1
        else:
            print('Candidato incorreto.')
    eleitor = 'n'
    
    # imprime o resultado
    senha = input('Digite a senha para finalizar: ')
    while True:
        if senha != sua_senha:
            print("Senha invalida. Tente novamente.")
        else:
            print('Eleitores: ',votacao,'\nCandidato1: ',candidatos[0],'\nCandidato2: ',candidatos[1],
            '\nCandidato3: ',candidatos[2],'\nNulo: ',candidatos[3],'\nBranco: ',candidatos[4],"\n")
            break

    # resultado da votação
    porcem = lambda candidato: 100*candidato/eleitores
    if candidatos[1] > candidatos[0] and candidatos[2] < candidatos[1]:
        print(f"Fim da eleição, o vencedor foi o Candidato2 com {porcem(candidatos[1])}% dos votos")
        empate = 'n'
    elif candidatos[2] > candidatos[0] and candidatos[1] < candidatos[2]:
        print(f"Fim da eleição, o vencedor foi o Candidato3 com {porcem(candidatos[2])}% dos votos")
        empate = 'n'
    elif candidatos[0] > candidatos[1] and candidatos[2] < candidatos[0]:
        print(f"Fim da eleição, o vencedor foi o Candidato1 com {porcem(candidatos[0])}% dos votos")
        empate = 'n'
    else:
        print(f'Houveram apenas votos em branco e/ou nulo: branco: {porcem(candidatos[4])}% e nulo: {porcem(candidatos[3])}%')

    # empate

    if candidatos[0] == candidatos[1] and candidatos[1] > candidatos[2]  and candidatos[2] < candidatos[0]:
        # restrição para desempate
        print("Houve empate! Preparem-se para o 2º turno!")
        numeros = ['1','2']
        print('Empate entre candidato1 e candidato2.')
        empate = 's'
    elif candidatos[2] == candidatos[0] and candidatos[2] > candidatos[1]  and candidatos[1] < candidatos[0]:
        print("Houve empate! Preparem-se para o 2º turno!")
        numeros = ['3','1']
        print('Empate entre candidato3 e candidato1.')
        empate = 's'
    elif candidatos[2] == candidatos[1] and candidatos[2] > candidatos[0]  and candidatos[0] < candidatos[1]:
        print("Houve empate! Preparem-se para o 2º turno!")
        numeros = ['3','2']
        print('Empate entre candidato3 e candidato2.')
        empate = 's'
    # reseta todos os votos para fazer o desempate
    candidatos = [0,0,0,0,0]
    votacao = 0
