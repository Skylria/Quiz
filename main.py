# -*- coding: utf-8 -*- 

import random
import os

# função para ler o arquivo de questões
def read_file():
    question = []
    questions = []
    f = open('questions.txt', 'r')
    lines = f.readlines()
    f.close()
    # adiciona uma quest a uma lista, e essa lista a uma lista maior com todas as quests
    for line in lines:
        question.append(line)
        if len(question) == 5:
            questions.append(question)
            question = []
    return questions

# função para atualizar o arquivo de questões
def update_file(quest, choices):
    name = 'questions.txt'
    f = open(name, 'a')
    f.write("\n" + quest + "\n")
    choice = choices.split('/')
    for x in choice:
        f.write(x + "\n")

# sfunção para embaralhar as questões
def sort_quests(quests):
    quest = random.choice(quests)
    return quest

# função para verificação da resposta correta
def verify_answer(ans, quest):
    if ans in quest[4]:
        verify = True
    else:
        verify = False
    return verify

# função que analisa e pontua as questões de acordo com a dificuldade

def score(quest, score, player):
    global endscore
    endscore = 0
    final_score = []
    if "Facil" in quest[0]:
        score += 1
    elif "Medio" in quest[0]:
        score += 3
    elif "Dificil" in quest [0]:
        score += 5
    endscore += score
    final_score.append(player)
    final_score.append(endscore)
    return final_score

# função para adicionar a pontuação do jogador
def records(player, score):
    player_score = []
    player_score.append(player)
    player_score.append(score)
    return player_score

# Função que escreve no arquivo de ranking as pontuações dos jogadores
def ranking_file(ranking_list):
    filesize = os.path.getsize("rank.txt")
    f = open('rank.txt', 'r')
    if (filesize == 0):
        f = open('rank.txt', 'w')
        f.write(str(ranking_list) + "\n")
        f.close
    else:
        f = open('rank.txt', 'a')
        f.write(str(ranking_list)+ "\n")
        f.close

# início do programa

score_one = 0
score_two = 0
player_one_score = 0
player_two_score = 0

answer = 4
rank = []

# Main Menu
while answer != 0: 
    print("Bem vindo a 'The Game of Thrones' O quiz!")
    print("----x*x* Menu: x*x*----\n1 - Iniciar o quiz \n2 - Customizar perguntas \n3 - Exibir Ranking \n0 - Sair \n----x*x*x*x*x*x*x*x----")

    answer = int(input())
    q_a = read_file()
    if answer == 1: 
    #Caso singleplayer 
        while True:
            # Verificação de jogadores ativos na partida
            print("\n1 - jogar solo ou \n2 - jogar com outra pessoa")
            first_input = int(input())
            # Menu de escolha de quantidade de jogadores
            if first_input == 1:
                player_one_score = 0
                # score_one = 0
                player_one = input("Digite a identificação do nobre guerreiro com 3 letras: ")
                while True:
                    if len(player_one) > 3:
                        print("Por favor digite uma identificação com no máximo 3 letras: ")
                    else:
                        multiplayer = False
                        for x in range (0, 6):
                            quest = sort_quests(q_a)
                            q_a.remove(quest)
                            for line in (range(0, len(quest) - 1)):
                                print(f"{quest[line]}", end ='')
                            ans = input().upper()
                            if ans == '0':
                                answer = 0
                                break
                            correct_answer = verify_answer(ans, quest)
                            if ans == " ":
                                correct_answer = False
                            if correct_answer:
                                print(" Boa jogada milord! Voce acertou!")
                                single_score = score(quest, score_one, player_one)
                                player_one_score += single_score[1]
                                records(player_one, player_one_score)
                                print(player_one_score)
                            else:
                                print("Dracarys! Voce errou!")
                        print('|JOGADOR|**************|PONTOS|\n')
                        p_one = []
                        p_one = records(player_one, player_one_score)
                        ranking_file(p_one)
                        print(f'  {player_one} ------------------> {player_one_score}\n')
                        break
            elif first_input == 2:
                player_one_score = 0
                player_two_score = 0
                while True:
                    player_one = input("Digite o nome do nobre guerreiro numero 1: ")
                    player_two = input("Digite o nome do nobre guerreiro numero 2: ")
                    if len(player_one) > 3 and len(player_two) > 3:
                        print("Por favor digite uma identificação com no máximo 3 letras: ")
                    else:
                        multiplayer = True
                        if answer == 1:
                            #Verificações do primeiro jogador
                            print(f" {player_one}! \nPrepare-se milord!")
                            #Escolhe seis perguntas e exibe para o primeiro jogador
                            for x in range(0, 6):
                                quest = sort_quests(q_a)
                                q_a.remove(quest)
                                for line in (range(0, len(quest) - 1)):
                                    print(f"{quest[line]}", end ='')
                                
                                ans = input().upper()
                                if ans == '0':
                                    answer = 0
                                    break
                                correct_answer = verify_answer(ans, quest)
                                if ans == " ":
                                    correct_answer = False
                                if correct_answer:
                                    print("Boa jogada milord! Voce acertou!")
                                    first_player_score = score(quest, score_one, player_one)
                                    player_one_score += first_player_score[1]
                                    records(player_one, player_one_score)
                                    print(player_one_score)
                                else:
                                    print("Dracarys! Voce errou!")
                            print(f"Obrigado por jogar {player_one} agora eh a vez do seu oponente!\n")
                            print(f" {player_two}! \nPrepare-se milord!")
                            #Escolhe seis perguntas e exibe para o segundo jogador
                            for x in range(0, 6):
                                quest = sort_quests(q_a)
                                q_a.remove(quest)
                                for line in (range(0, len(quest) - 1)):
                                    print(f"{quest[line]}", end ='')
                                
                                ans = input().upper()
                                if ans == '0':
                                    answer = 0
                                    break
                                correct_answer = verify_answer(ans, quest)
                                if ans == " ":
                                    correct_answer = False
                                if correct_answer:
                                    print("Boa jogada milord! Voce acertou!")
                                    second_player_score = score(quest, score_two, player_two)
                                    player_two_score += second_player_score[1]
                                    records(player_two, player_two_score)
                                    print(player_two_score)
                                else:
                                    print("Dracarys! Voce errou!")
                            print('|JOGADOR|**************|PONTOS|')
                            p_one = []
                            p_one = records(player_one, player_one_score)
                            ranking_file(p_one)
                            print(f'  {player_one} ------------------> {player_one_score}')
                            p_two = []
                            p_two = records(player_two, player_two_score)
                            ranking_file(p_two)
                            print(f'  {player_two} ------------------> {player_two_score}')
                            break
                        #Enquanto não for digitado um valor válido, não sai do loop
            else:
                print("Digite um valor valido!")
    
    # para caso o jogador queira adicionar uma pergunta ao jogo direto no arquivo de texto!
    if answer == 2:
        question = input("Fique a vontade e digite a pergunta que deseja inserir no nosso banco de dados para tornar seu jogo ainda mais divertido: ")
        print("Siga esse modelo para as alternativas - [A - São Paulo/B- Rio de Janeiro/C- Alemanha/C")
        print("As alternativas devem ser separadas por vírgula e no final a resposta correta em letra maiúscula!")
        choices = input("Digite as alternativas que deseja inserir e a resposta correta seguindo o modelo acima: ")
        update_file(question, choices)
    
    if answer == 3:
        print('|JOGADOR|**************|PONTOS|\n')
        f = open('rank.txt', 'r')
        lines = f.readlines()
        f.close()
        #Exibe todas as pontuações cadastradas no arquivo de ranking
        for line in lines:
            print(f' {line[2:5]} ------------------> {line[8:-2]}')
        
print("Obrigado por jogar!")