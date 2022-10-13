import random
import string

print("Welcome to hangman lets start now")
list_of_words = ("december","dream","derivative","factorial","gorilla","banana","january","beowulf","technoblade","discontinuous","eccentric")
word = random.choice(list_of_words)
letters = len(word)
list_ = list(word)
l = list(word)
word_ = " ".join(list_)
brackets = []
backup_brackets = []
def no_of_brackets():
    x = 0
    while x != letters:
        brackets.append("_")
        x += 1
    space = " ".join(brackets)
    print (space)
def backup_():
    y = 0
    while y != letters:
        backup_brackets.append("_")
        y += 1
    sp = " ".join(brackets)
    return sp

def guessing ():
    life = 3
    guess = ""
    while list_ != backup_brackets:
        guess = str.lower(input("Enter any letter or a word: "))
        if guess == word:
            s = " ".join(l)
            print(s)
            print("Congratulations you guessed the correct word") 
            break
        if guess in list(string.digits) or guess in list(string.punctuation):
             print("Try Again")
        if guess in list_:
            for i in list_:
                if guess in i:
                    pos = list_.index(guess)
                    list_[pos] = "_"
                    brackets[pos] = guess
                    space = " ".join(brackets)
            print(space)
        else :
            life -= 1
            print (f"Wrong, Try again. Your Chance remaining {life}")
        if life == 0:
            print("GameOver")
            print("The correct word is")
            print(" ".join(l))
            break
    else:
        print("Win")
no_of_brackets()
backup_()
guessing()
        

