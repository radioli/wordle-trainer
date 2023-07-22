# oblicz wagi slow 1-pasuje litera 1-pasuje miejsce czyli max 10 za poprawne slowo
# zrobi potem slownik z odpowiednimi wagami
# drzewo gdzie wezly beda wagami
# user robi input i przechodz pomiedzy wagami az do znalezienia
import random
from collections import defaultdict
from colorama import Fore, Back, Style
import os


class GameRender():
    def __init__(self):
        self.yellow = Fore.YELLOW
        self.green = Fore.GREEN
        self.white = Fore.WHITE
        self.words_to_render = []
        self.history = ''

    def decode_color(self, labeled_letter):
        if labeled_letter['color'] == 'y':
            return self.yellow
        elif labeled_letter['color'] == 'g':
            return self.green
        elif labeled_letter['color'] == 'w':
            return self.white

    def prepare_word_for_render(self, labeled_letter):
        return self.decode_color(labeled_letter) + labeled_letter["letter"] + " "

    def add_letter_to_render(self, labeled_letter):
        letter_to_render = self.prepare_word_for_render(
            labeled_letter)  # here string with color of one letter
        self.words_to_render.append(letter_to_render)

    def clear_screen(self):
        os.system('clear')

    def render_word(self):
        for letter in self.words_to_render:
            self.history+=letter+" "
        self.history+='\n'
        self.clear_words_to_render()

    def clear_words_to_render(self):
        self.words_to_render = []
    def print_history(self):
        self.clear_screen()
        print(self.history)

class WordleGameAnalyzer:
     def __init__(self):
       pass  

def WordlePlayer(WordleGame):
    def __init__(self, name):
        self.name = name
        self.player_logs = []

    def add_word(self):
        return input()

class WordleGame(GameRender):

    def __init__(self):
        super().__init__()
        self.words = self.__read_words()
        self.answer = random.choice(self.words)
        self.score_pools = self.__initialize_scores_for_words()

    def __read_words(self):
        words = []
        with open('words.txt') as f:
            words = f.read().splitlines()
        return words

    def label_letter_from_input(self, input):
        for index, character in enumerate(input):
            list_of_occurences = self.__find_occurrences(
                self.answer, character)
            if index in list_of_occurences:
                labeled_letter = {"color": "g", "letter": character}
            elif len(list_of_occurences) > 0:
                labeled_letter = {"color": "y", "letter": character}
            else:
                labeled_letter = {"color": "w", "letter": character}
            self.add_letter_to_render(labeled_letter)

    def calculate_score(self, word: str):
        # count if
        current_score = 0
        point_for_ok_letter = 1
        point_for_ok_placement = 1
        for index, character in enumerate(word):
            list_of_occurences = self.__find_occurrences(
                self.answer, character)
            multiplier = len(list_of_occurences)
            if multiplier == 0:
                continue
            # count scores
            if index in list_of_occurences:
                current_score += multiplier*point_for_ok_letter
                current_score += point_for_ok_placement
            else:
                current_score += multiplier*point_for_ok_letter
        return current_score

    def __find_occurrences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    def __initialize_scores_for_words(self):
        score_pools = defaultdict(list)
        for word in self.words:
            score_pools[self.calculate_score(word)].append(word)
        return score_pools

    def get_words_by_score(self, score):
        return self.score_pools[score]

    def get_list_of_scores(self):
        print(self.score_pools.keys())

#todo add main game loop
def wordle_game_loop():
    wordle_instance = WordleGame()
    print('answer:' + wordle_instance.answer)

    while True:
        print(Fore.WHITE + "Your input:", end=' ')
        x = input()
        score = wordle_instance.calculate_score(x)  # data sent to renderer
        #print(score)
        wordle_instance.label_letter_from_input(x)
        wordle_instance.render_word()
        wordle_instance.print_history()
        if(score == 10):
            print('WIN')
            break


#no repeated letters
def main():
    """ Main program """
    # Code goes over here.
    wordle_game_loop()


if __name__ == "__main__":
    main()
