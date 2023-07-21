# oblicz wagi slow 1-pasuje litera 1-pasuje miejsce czyli max 10 za poprawne slowo
# zrobi potem slownik z odpowiednimi wagami
# drzewo gdzie wezly beda wagami
# user robi input i przechodz pomiedzy wagami az do znalezienia
import random
from collections import defaultdict
from colorama import Fore, Back, Style

class WordleGame():

    def __init__(self):
        self.words = self.__read_words()
        self.answer = random.choice(self.words)
        self.score_pools = self.__initialize_scores_for_words()

    def __read_words(self):
        words = []
        with open('words.txt') as f:
            words = f.read().splitlines()
        return words

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
                print(Fore.WHITE + character, end=" ")
                continue
            # count scores
            if index in list_of_occurences:
                current_score += multiplier*point_for_ok_letter
                current_score += point_for_ok_placement
                print(Fore.GREEN + character, end=" ")
            else:
                current_score += multiplier*point_for_ok_letter
                print(Fore.YELLOW + character, end=" ")

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


def WordlePlayer(WordleGame):
    def __init__(self, name):
        self.name = name

    def add_word(self):
        return input()


def check_if_words_exists(input):
    pass


def wordle_game_loop():
    wordle_instance = WordleGame()
    print('answer:' + wordle_instance.answer)
    while True:
        print('\nstart typing\n')
        x = input()
        score = wordle_instance.calculate_score(x)
        if(score == 10):
            print("win")
            break


#no repeated letters
def main():
    """ Main program """
    # Code goes over here.
    wordle_game_loop()


if __name__ == "__main__":
    main()
