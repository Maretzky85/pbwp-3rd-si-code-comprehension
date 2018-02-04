#program runs a guess game. Firstly choosing random number from 1 to 20, and ask for quess. You can guess up to 6 times.
import random #import random library

guesses_taken = 0 #Assign 0 to guesses_taken variable

print('Hello! What is your name?') #Print text to console
myName = input() #Ask user for input, waits for enter and assign input as str to variable myName

number = random.randint(1, 20) #assigning to variable a randomly choosed integer from range 1-20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #prints a string in variable name inside

while guesses_taken < 6: #creates loop that compares guesses_taken var to 6 integer, and runs until var reaches 6, than stops. 6 loop will not be executed
    print('Take a guess.') #prints a string
    guess = input() #asks for user keyboard input, waits for enter and assigning inpupt as str to var guess
    guess = int(guess) #changes var guess to int

    guesses_taken += 1 #adds +1 to var guesses taken

    if guess < number: #creates if condition that takes inputed guess variable and compares to number variable, checking if guess var is lower than number var
        print('Your guess is too low.') #if condition is met, prints a str to console

    if guess > number: #creates if condition that takes inputed guess variable and compares to number variable, checking if guess var is higher than number var
        print('Your guess is too high.') #if condition is met, prints a str to console

    if guess == number:#creates if condition that takes inputed guess variable and compares to number variable, checking if guess var equals number var
        break #exits loop

if guess == number: #after loop, if guess var equals number var execute code bolew
    guesses_taken = str(guesses_taken) #changes var guesses_taken from var to str
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #prints str +2 variables in

if guess != number: #another check, if var guess differs from var number execute code below
    number = str(number) #changes var number to str
    print('Nope. The number I was thinking of was ' + number) #print str and var number at end
