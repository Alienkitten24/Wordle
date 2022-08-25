import random


def selectWord():
    file = open('listOfWordleWords.txt')
    words = file.readlines()
    myWord = random.choice(words)
    return myWord


def checkWordWithList(toBeChecked):
    file = open('listOfWordleWords.txt')
    words = file.read().splitlines()
    return bool(toBeChecked in words)


correctWord = selectWord()
numberOfGuesses = 0
colors = []
maxWordLength = 5
remainingLetters = ""

while numberOfGuesses < 6:
    #set colors to 5 greys
    colors = ['\U00002B1C'] * maxWordLength

    guess = input(">").lower()

    #checks if guess is valid
    if len(guess) != maxWordLength or not guess.isalpha():
        print(f"{maxWordLength} letter words only!")
    elif not checkWordWithList(guess):
        print("Not in word list!")

    #main logic
    else:
        remainingLetters = guess
        #green logic
        for i in range(len(guess)):
            if guess[i] == correctWord[i]:
                colors[i] = '\U00002705'  #green
                remainingLetters = remainingLetters.replace(guess[i], "_")

        #yellow logic
        for i in range(len(guess)):
            if remainingLetters[i] in correctWord:
                colors[i] = '\U00002747'  #yellow
                remainingLetters = remainingLetters.replace(guess[i], "_")

        print(colors)
        numberOfGuesses += 1

    if colors == ['\U00002705']*5:
        print("Well Done")
        break

print(f"The word was {correctWord}")
print(f"finished in {numberOfGuesses}")
