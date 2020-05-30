import random

def welcome():
    user_name = input("Enter your name : ")
    print("Welcome to the hangman game "+ user_name)
    
    print("Try to guess the word in 10 tries or less")
    HangmanGame()
    print()


def HangmanGame():
    word = random.choice(['python','django','flask','jinja','sql','pip'])
    ValidLetters = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns = 10
    guessed = ''
    while len(word)>0:
        dsp = ''
        missed = 0
        for letter in word:
            if letter in guessed:
                dsp = dsp + letter
            else:
                dsp = dsp + '_'  +' '
                missed+=1
        if dsp == word:
            print(dsp)
            print("Congrats!!! You got the word. The word is : ", word)
            break
        print("Guess the word : ",dsp)
        guess = input()
        if guess in ValidLetters:
            guessed = guessed + guess
        else:
            print(" Oops!!! try the next letter :")
            guess = input().lower()
        
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print(" o")
            if turns == 8:
                print(" o")
                print(" |")
            if turns == 7:
                print(" o")
                print(" |-")
            if turns == 6:
                print(" o")
                print("-|-")
            if turns == 5:
                print(" o") 
                print("-|-")
                print("  \\")
            if turns == 4:
                print(" o")
                print("-|-")
                print("/ \\")
            if turns == 3:
                print("  o")
                print("  |-")
                print(" / \\_")
            if turns == 2:
                print("  o")
                print(" -|-")
                print("_/ \\_")
            if turns == 1:
                print("You have lost your chance")
                print("Sorry, you failed to guess the right word.")
                break

# pagain = int(input('Enter 1 to play again : '))
# if pagain == 1:
welcome()
# else:
    # print("Thank you for playing Hangman Game")

