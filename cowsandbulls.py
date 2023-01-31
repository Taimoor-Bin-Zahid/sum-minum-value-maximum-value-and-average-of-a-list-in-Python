######################################## Random Function #################################

import random
def randomNumber():
    generateNum = ''
    while len(generateNum) < 4:
        currentNum = str(random.randint(0,9))
        if not currentNum == generateNum:
            generateNum += currentNum
    return generateNum


####################################### Cow and Bull Game ################################

number_of_guess = 6
generateNum = randomNumber()
while number_of_guess > 0:
    currentGuess = int(input("Enter your Guess: "))
    currentGuess = str(currentGuess)
    bulls=0
    cows=0
    print(generateNum)
    for i in range(len(generateNum)):
        if currentGuess[i] in generateNum:
            if currentGuess[i] == generateNum[i]:
                bulls+=1
            else:
                cows+=1
    print(f'Cows: {cows}, Bulls: {bulls}')
    if not bulls < 4:
        print('You win!')
        break
    number_of_guess -= 1
if not number_of_guess > 0:
    print(f"You ran out of tries you lose!!! The answer is {generateNum}")
