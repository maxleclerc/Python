# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:17:41 2019

@author: Maxence
"""

import random

HANGMAN_PICS = ['''
                +---+
                    |
                    |
                    |
                   ===''','''
                +---+
                0   |
                    |
                    |
                   ===''','''
                +---+
                0   |
                |   |
                    |
                   ===''','''
                +---+
                0   |
               /|   |
                    |
                   ===''','''
                +---+
                0   |
               /|\  |
                    |
                   ===''','''
                +---+
                0   |
               /|\  |
               /    |
                   ===''','''
                +---+
                0   |
               /|\  |
               / \  |
                   ===''','''
                +---+
               [0   |
               /|\  |
               /    |
                   ===''','''
                +---+
               [0]  |
               /|\  |
               / \  |
                   ===''']

words = {'Colors' : 'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes' : 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruit' : 'apple orange lemon lime pear watermelon grape grapefruit cherry baanana cantaloupe mango strawberry tomato'.split(),
         'Animals' : 'ant baboon badger bat bear beaver camel cat cobra cougar coyote crab crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    # this function returnsa random sstring from the passed dictionnary of list of strings and its key
    #first, randomly select a key from the dictionnary
    wordKey = random.choice(list(wordDict.keys()))

    #second, randomly select a word from the key's list in the dictionnary
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks: # show the secret word with space between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #return the letter the player entered. This function makes sure the player entered a single letter and not something else
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter,')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #this function returns True if the player wants to play again; otherwise, it returns False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

def foncDifficulty():
    difficulty = ''
    while True:
        print('Enter difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()
        if difficulty == 'E':
            break
        if difficulty == 'M':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            break
        if difficulty == 'H':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            del HANGMAN_PICS[6]
            del HANGMAN_PICS[5]
            break
        
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

foncDifficulty()

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    
    #Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        #Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        #Check if the player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True   
    
    #Ask the player if they want to play again ( but only if the gale is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
