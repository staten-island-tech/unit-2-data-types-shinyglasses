'''1. Using the "input" method in Python, ask a user to input a sentence. 
Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan in Pseudo-code using comments.
 Then craft the function. 
2. Mad Libs Project
- Create variables representing at least 2 verbs, 1 noun, 1 number,
and 1 celebrity guest. You may include any additional
variables/madlibs you want
- Receive user input and assign that user input to the variables in
step 1
- Create variable “Madlib” represented by F String that tells a
story using the variables from step 1
- Print the f string after the user has input data'''

def num():
    sentence = input('Write a sentence').split()
    print(len(sentence))

def madlibs():
 
    noun_one = input('noun?')
    verb_one = input('action verb?')
    guest = input('celebrity guest?')
    verb_two = input('verb?')
    number = input('number?')  
    noun_two = input('singular noun?')
    verb_three = input('verb?')
    disease = input('disease?')
    madlib = (f'It was a dark and stormy {noun_one}. You were planning to {verb_one} before it began raining. Suddenly, your camera showed {guest} {verb_two} toward your house! They were holding {number} {noun_two}! You let them in and they {verb_three} with their {number} {noun_two} You died..... The doctors said it was from {disease}')
    print(madlib)

'''## Challenge
Let's create a function that determines if a number is odd or even
## Challenge
Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 

## Challenge

Create a function that accepts an input and determines all factors of the number. 

## Challenge 

Create a function that accepts 2 arguments. Find the greatest common factor between those numbers. 
'''
def even_or_odd():
    num = int(input('Write a number'))
    if type(num/2) == float:
        print('This is odd')
    else:
        print("This is even")

def tip():
    quality = ["bad", "okay", "good", "great"]
    tip = 0
    bill = int(input('What was the price of your bill?'))
    while bill == 0:
        bill = int(input('YO WHY ARE YOU TRYING TO CALCULATE A TIP WHEN THE BILL IS NOTHING?!?!?!?! PLEASE GIVE AN ACTUAL NUMBER!!!'))
    quality = input('Write the quality of the service: bad, okay, good, or great.').strip().lower()
    if quality == "bad":
        tip = 0
    elif quality == "okay":
        tip = .15 * bill
    elif quality == "good":
        tip = .2 * bill        
    elif quality == 'great':
        tip = .25 * bill
    print(f'Your final bill is {bill + tip}, since the bill is {bill} and the tip is {tip}')

def factors():
    factors = []
    num = int(input("What's your number? ONLY INTEGERS!!!!"))
    divisor = 1
    for i in range(num):
        if type(num//divisor) == int:
            factors.append(num//divisor)
        divisor += 1
    factors = list(set(factors))
    print(f'Factors are {factors}')

def gcf(num, num2):
    gcf = 0  
    for i in range(1, num + 1):
        if num%i == 0 and num2%i == 0:
           gcf = i
    print(f'The greatest common factor of {num} and {num2} is {gcf}')
#iterate over all common factors and it ends when you get to the gcf.
