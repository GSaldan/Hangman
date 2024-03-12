import random
from words import words_easy, words_hard, words_medium
import string
# disclaimer: the game is in PT/BR because it was made for my friends to play, but you can 
# change the lists in the "words" files to your language of preference


# instruções: escolha entre 1 das 3 dificuldades e o computador vai escolher uma palavra
# tente adivinhar a palavra chutando letra por letra.


def word_pick():
    difficulty = 'a'

    while difficulty != 'f' or difficulty != 'm' or difficulty != 'd':

        difficulty = input('Escolha entre fácil (f) - medio (m) - dificil (d): ')
        if difficulty == 'f':
            # picks a random word from the easy category
            word = random.choice(words_easy)
            # exclude words with special characters
            while 'á' in word or 'ã' in word or 'â' in word or 'é' in word or 'ê' in word or 'í' in word or 'ó' in word \
                    or 'ô' in word or 'ú' in word or 'ç' in word:
                word = random.choice(words_easy)
            return word.upper()
        elif difficulty == 'm':
            # picks a random word from the medium category
            word = random.choice(words_medium)
            # exclude words with special characters
            while 'á' in word or 'ã' in word or 'â' in word or 'é' in word or 'ê' in word or 'í' in word or 'ó' in word \
                    or 'ô' in word or 'ú' in word or 'ç' in word:
                word = random.choice(words_medium)
            return word.upper()
        elif difficulty == 'd':
            # picks a random word from the hard category
            word = random.choice(words_hard)
            # exclude words with special characters
            while 'á' in word or 'ã' in word or 'â' in word or 'é' in word or 'ê' in word or 'í' in word or 'ó' in word \
                    or 'ô' in word or 'ú' in word or 'ç' in word:
                word = random.choice(words_hard)
            return word.upper()
        else:
            print('Dificuldade invalida, digite (f), (m) ou (d)')


def hangman():
    word = word_pick()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the players has used
    # keep track of player's lives/tries
    lives = 6

    # user input
    while len(word_letters) > 0 and lives > 0:
        # show the word minus the letters the player have not guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('A palavra é', ' '.join(word_list))

        # show the guessed letters so far
        print(f'Você tem {lives} vidas e ja usou as letras: ', ' '.join(sorted(used_letters)))

        player_letter = input('Escolha uma letra: ').upper()

        if player_letter in alphabet - used_letters:
            used_letters.add(player_letter)
            if player_letter in word_letters:
                word_letters.remove(player_letter)
            else:
                lives = lives - 1

        elif player_letter in used_letters:
            print('Você ja usou essa letra, tente outra')

        else:
            print('Caractére invalido, por favor tente novamente')
    # win condition (lose or win)
    if lives <= 0:
        print('Você perdeu =(')
        print(f'A palavra era - {word}')
    else:
        print(f'Você acertou a palavra - {word}!!!')
        print(f'Em {len(used_letters)} tentativas')
    reset()


def reset():
    # give the option to restart or quit the game
    restart = input('Você quer recomeçar (s) para sim e (n) para não: ')

    if restart == 's':
        hangman()
    elif restart == 'n':
        print('Obrigado por jogar!')
    else:
        print('Resposta invalida, use apenas (s) ou (n)')
        reset()


hangman()
