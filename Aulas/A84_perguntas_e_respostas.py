perguntas = [
    {
        'Pergunta': 'Quanto é 5 + 8?',
        'Alternativas': ['11', '12', '13', '14', '15'],
        'Alternativa correta': '3'
    },

    {
        'Pergunta': 'Quanto é 3 + 8 * 2?',
        'Alternativas': ['18', '19', '20', '21', '22'],
        'Alternativa correta': '2'
    },

    {
        'Pergunta': 'Quanto é 10 + 2 * 0?',
        'Alternativas': ['0', '5', '6', '10', '12'],
        'Alternativa correta': '4'
    },

    {
        'Pergunta': 'Pronto para a última pergunta?',
        'Alternativas': ['Sim', 'Não', 'Depende'],
        'Alternativa correta': '3'
    },

    {
        'Pergunta': 'Quantas letras tem o alfabeto?',
        'Alternativas': ['26', '27', '28', '24', '25'],
        'Alternativa correta': '1'
    }
]

print('Não se esqueça, sua resposta precisa ser o número da alternativa.\n')

pontuacao = 0

for pergunta in range(len(perguntas)):
    print('Pergunta:', perguntas[pergunta].get('Pergunta'), '\n')

    alternativas = perguntas[pergunta].get('Alternativas')

    print('Alternativas:')

    for alternativas, valores in enumerate(alternativas):
        print(f'{alternativas + 1}) {valores}')

    resposta_do_usuario = input('\nEscolha uma opção: ')

    alternativa_correta = perguntas[pergunta].get('Alternativa correta')
    
    if resposta_do_usuario == alternativa_correta:
        print('Certa a resposta.\n')

        pontuacao += 1

    else:
        print('Errou.\n')

if pontuacao == 0:
    print('Você errou todas as perguntas!')

elif pontuacao == len(perguntas):
    print(f'Parabéns, você acertou todas as {len(perguntas)} perguntas!')

else:
    print(f'Você acertou {pontuacao} de {len(perguntas)} perguntas!')
