from art import logo, vs
from data import data
import random
from replit import clear


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """takes the guess and followers count of a and b and returns if they got it right"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while(account_a == account_b):
        account_b = random.choice(data)

    print(f"compare A : {format_data(account_a)}")
    print(vs)
    print(f"against B : {format_data(account_b)}")

    guess = input("Who has more followers? A or B : ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    clear()

    if(is_correct):
        score += 1
        print(f"You are right, current socre : {score}")
    else:
        print(f"you are wrong, final score : {score}")
        game_should_continue = False

