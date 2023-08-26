import random

secret_number = random.randint(1,50)

print("Welcome to the Guess the Number Game!")
print("Here I am guessing number from 1 to 50. can you guess the number?")


while True:
    guess = int(input("Enter your guessing number: "))

    if guess == secret_number:
        print("Congratulations! You have guesses correct number.")
        break
    elif guess > secret_number:
        print("Your guess is higer.Please try again.")
    else:
        print("Your guess is lower. Please try again ")

    
    
        

    
        

