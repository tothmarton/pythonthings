import random

def dice_throwing ():
    return (random.randrange(6))+1

def who_is_the_winner():
    if player1.point > player2.point:
        print(" " + player1.player_name + ", you are the winner! :) ")
        print(" " + player2.player_name + ", maybe next time! :( ")
    elif player2.point > player1.point:
        print(" " + player2.player_name + ", you are the winner! :) ")
        print(" " + player1.player_name + ", maybe next time! :( ")
    elif player1.point == player2.point:
        print(" " + player1.player_name + ", " + player2.player_name + "that's a draw. Let's play again!")

class player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.first = ""
        self.second = ""
        self.third = ""
        self.fourth = ""
        self.fifth = ""
        self.combination_name = ""
        self.point = 0
    def generate_five_dice_throwing(self):
        self.first = dice_throwing()
        self.second = dice_throwing()
        self.third = dice_throwing()
        self.fourth = dice_throwing()
        self.fifth = dice_throwing()
    def print_dice_values(self):
        print (" " + self.player_name + "'s dice values: " + str(self.first) + "; " + str(self.second) + "; " + str(self.third) + "; " + str(self.fourth)
         + "; " + str(self.fifth))
    def yathzee_check(self):
        if self.first == self.second and self.second == self.third and self.third == self.fourth and self.fourth == self.fifth:
            self.combination_name="Yathzee"
            self.point=50
    def pair_check(self):
        value_list = [self.first, self.second, self.third, self.fourth, self.fifth]
        for i in range(0,5):
            equal_counter = 0
            for j in range(0,5):
                if j!=i and value_list[i] == value_list[j]:
                    equal_counter +=1
            if equal_counter == 1:
                return True
    def three_of_a_kind_and_full_house_check(self):
        value_list = [self.first, self.second, self.third, self.fourth, self.fifth]
        for i in range(0,5):
            equal_counter = 0
            for j in range(0,5):
                if j!=i and value_list[i] == value_list[j]:
                    equal_counter +=1
            if equal_counter == 2:
                sum_of_dice_values = 0
                for i in range(0,5):
                    sum_of_dice_values += (value_list[i])
                if sum_of_dice_values > self.point:
                    self.point = sum_of_dice_values
                    self.combination_name="Three of a kind"
                if self.pair_check() == True:
                    if 25 > self.point:
                        self.point=25
                        self.combination_name="Full house"
                    break
    def four_of_a_kind_check(self):
        value_list = [self.first, self.second, self.third, self.fourth, self.fifth]
        for i in range(0,5):
            equal_counter = 0
            for j in range(0,5):
                if j!=i and value_list[i] == value_list[j]:
                    equal_counter +=1
            if equal_counter == 3:
                sum_of_dice_values = 0
                for i in range(0,5):
                    sum_of_dice_values += (value_list[i])
                if sum_of_dice_values > self.point:
                    self.point = sum_of_dice_values
                    self.combination_name="Four of a kind"
    def straight_check(self):
        value_list = [self.first, self.second, self.third, self.fourth, self.fifth]
        one = False
        two = False
        three = False
        four = False
        five = False
        six = False
        for i in range(0,5):
            if value_list[i] == 1:
                one= True
            elif value_list[i] == 2:
                two= True
            elif value_list[i] == 3:
                three= True
            elif value_list[i] == 4:
                four= True
            elif value_list[i] == 5:
                five= True
            elif value_list[i] == 6:
                six= True
        if one and two and three and four and five:
            if 40 > self.point:
                self.point = 40
                self.combination_name="Large Straight"
        elif two and three and four and five and six:
            if 40 > self.point:
                self.point = 40
                self.combination_name="Large Straight"
        elif one and two and three and four:
            if 30 > self.point:
                self.point = 30
                self.combination_name="Small Straight"
        elif two and three and four and five:
            if 30 > self.point:
                self.point = 30
                self.combination_name="Small Straight"
        elif three and four and five and six:
            if 30 > self.point:
                self.point = 30
                self.combination_name="Small Straight"
    def chanche_calc(self):
        if (self.first + self.second + self.third + self.fourth + self.fifth) > self.point:
            self.point = self.first + self.second + self.third + self.fourth + self.fifth
            self.combination_name="Chance"
    def print_score(self):
        print(" " + self.player_name + ", that's a " + self.combination_name + ". Your sum point is: " + str(self.point))
    def get_point(self):
        self.yathzee_check()
        self.straight_check()
        self.three_of_a_kind_and_full_house_check()
        self.four_of_a_kind_check()
        self.chanche_calc()
        self.print_score()

player_name = input(" Please, enter the 1st player name: ")
player1 = player(player_name)
player_name = input(" Please, enter the 2nd player name: ")
player2 = player(player_name)

print("***********************************************")

print(" Let's play some Yathzee! " + player1.player_name + " VS " + player2.player_name )

print("***********************************************")

player1.generate_five_dice_throwing()
player1.print_dice_values()
player2.generate_five_dice_throwing()
player2.print_dice_values()

print("***********************************************")

player1.get_point()
player2.get_point()

print("***********************************************")

who_is_the_winner()
