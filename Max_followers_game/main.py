# importing the required to be dated from other module's
from art import logo, vs
from game_data import data
import random

# print the header of the game
print(logo)
# compare to check who has the lower value


def compare(followers_1, followers_2):
    if followers_1 > followers_2:
        return True
    else:
        return False

# Get random entity from the data available


def get_random_entity():
    entity = random.choice(data)
    return entity

# initialize the comparison entities


def intialize_entity():
    entity_dic = {}
    entity_a = get_random_entity()
    entity_b = get_random_entity()
    
    while entity_a['name'] == entity_b['name']:
        entity_b = get_random_entity()
    
    entity_dic['a'] = entity_a
    entity_dic['b'] = entity_b
    return entity_dic

# create function to print data in formatted form


def format_print(to_print_dic, key):
    print(f" Entity_{key} : {to_print_dic['name']} , a {to_print_dic['description']} from {to_print_dic['country']}.")
    

# Functionality for the game

def game():
    print("Guess who  has more followers on instagram.")
    should_continue = True
    score = 0
    rand_dic = {}
    rand_dic = intialize_entity()

    while should_continue:
        format_print(rand_dic['a'], 'a')
        print(vs)
        rand_dic['b'] = get_random_entity()
        # What if the random choice is same as first choice
        while rand_dic['a']['name'] == rand_dic['b']['name']:
            rand_dic['b'] = get_random_entity()
        
        format_print(rand_dic['b'], 'b')
        selected_choice = input("Who has more followers! A or B: ").lower()
        other_choice = ""
        
        # we get the other Choice
        for key in rand_dic:
            if key != selected_choice:
                other_choice = key

        is_answer_right = compare(rand_dic[selected_choice]['follower_count'], rand_dic[other_choice]['follower_count'])
        if is_answer_right:
            score += 1
            # replace the first choice with the other option
            rand_dic['a'] = rand_dic[other_choice]
            print(f"You are right! your current score : {score}")
        else:
            print(f"Sorry that's wrong! your Final score : {score}")
            should_continue = False
        
# call game function to start playing game


game()
