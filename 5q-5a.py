import random

def fill_array(array_name, type):
    array_name=[]
    for i in range(0,5):
        array_name.append(input("Enter the "+ str(type) +" number " + str(i) + ": "))
    return array_name

question_array = fill_array("question_array", "question")
answer_array = fill_array("answer_array", "answer")

question_random_numbers=[]
answer_random_numbers=[]
out_counter = 0

while out_counter < 5:
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    rand_number_uniq = False
    while rand_number_uniq == False:
        rand_number = random.randrange(5)
        if rand_number not in question_random_numbers:
            print("Question: " + question_array[rand_number])
            question_random_numbers.append(rand_number)
            rand_number_uniq = True
    rand_number_uniq = False
    while rand_number_uniq == False:
        rand_number = random.randrange(5)
        if rand_number not in answer_random_numbers:
            print("Answer : " + answer_array[rand_number])
            answer_random_numbers.append(rand_number)
            out_counter += 1
            rand_number_uniq = True
