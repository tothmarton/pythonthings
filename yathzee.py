import random

def dice_throwing ():
    return (random.randrange(6))+1

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
        print (self.player_name + "'s dice values: " + str(self.first) + "; " + str(self.second) + "; " + str(self.third) + "; " + str(self.fourth)
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
                self.combination_name="Three of a kind"
                sum_of_dice_values = 0
                for i in range(0,5):
                    sum_of_dice_values += (value_list[i])
                self.point = sum_of_dice_values
                if self.pair_check() == True:
                    self.combination_name="Full house"
                    self.point=25
                    break
    def four_of_a_kind_check(self):
        value_list = [self.first, self.second, self.third, self.fourth, self.fifth]
        for i in range(0,5):
            equal_counter = 0
            for j in range(0,5):
                if j!=i and value_list[i] == value_list[j]:
                    equal_counter +=1
            if equal_counter == 3:
                self.combination_name="Four of a kind"
                sum_of_dice_values = 0
                for i in range(0,5):
                    sum_of_dice_values += (value_list[i])
                self.point = sum_of_dice_values

player_name = input("Please, enter the 1st player name: ")
player1 = player(player_name)
player_name = input("Please, enter the 2nd player name: ")
player2 = player(player_name)

print("Let's play some Yathzee! " + player1.player_name + " VS " + player2.player_name )

i=0
while i<10000:
    print(i)
    player1.generate_five_dice_throwing()
    player1.print_dice_values()
    player2.generate_five_dice_throwing()
    player2.print_dice_values()
    player1.yathzee_check()
    player1.three_of_a_kind_and_full_house_check()
    i+=1
    print(player1.combination_name)
    print(player1.point)
