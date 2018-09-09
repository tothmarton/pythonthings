import random

word_list = ['apple','computer','running','car','hangman','table','carpenter','flower','desktop','python']

class player:
    def __init__(self, player_name):
        self.name = player_name
        self.fail_points = 0
        self.act_letter = ""

    def guess_letter(self):
        self.act_letter = input(" " +self.name+ ", please, guess a letter: ")

class game:
    def __init__(self, word_list):
        self.randomised_word = self.randomise_game_word(word_list)
        self.word_letter_count = len(self.randomised_word)
        self.known_word = self.create_known_word(self.word_letter_count)
        self.ready = False

    def randomise_game_word(self, word_list):
        return word_list[random.randrange(len(word_list))]

    def create_known_word(self, letter_count):
        known_word = ""
        for i in range(0,letter_count):
            known_word = known_word + "_"
        return known_word

    def check_if_letter_mached(self, guessed_letter, player):
        if self.randomised_word.count(guessed_letter) > 0:
            temp_known_word = ""
            for i in range(0,self.word_letter_count):
                if (self.randomised_word[i] == guessed_letter) and (self.known_word[i] == "_"):
                    temp_known_word = temp_known_word + guessed_letter
                else:
                    temp_known_word = temp_known_word + self.known_word[i]
            print(temp_known_word)
            self.known_word = temp_known_word
        elif self.randomised_word.count(guessed_letter) == 0:
            player.fail_points =+ 1

    def check_if_ready(self):
        isReadylocal = True
        for ch in self.known_word:
            if ch == "_":
                isReadylocal = False
        if isReadylocal == True:
            self.ready = True

def main():
    this_game = game(word_list)
    print(this_game.randomised_word)
    print(this_game.word_letter_count)
    print(this_game.known_word)
    player1 = player(input(" Please, enter the 1st player name: "))
    player2 = player(input(" Please, enter the 2nd player name: "))
    while this_game.ready == False:
        if player1.fail_points < 8:
            player1.guess_letter()
            this_game.check_if_letter_mached(player1.act_letter, player1)
            this_game.check_if_ready()
            print(this_game.ready)
        if player2.fail_points < 8:
            player2.guess_letter()
            this_game.check_if_letter_mached(player2.act_letter, player2)
            this_game.check_if_ready()
            print(this_game.ready)

main()
