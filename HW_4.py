# task_1
import random

number_to_guess = random.randint(1, 10)
answer = input('Guess the number from 1 to 10')
if answer.isdigit():
    true_answer = int(answer)
else:
    print('Answer is not valid!')
    true_answer = None
if true_answer == number_to_guess:
    print('Correct!')
elif true_answer != number_to_guess:
    print(f'Incorrect, the answer is {number_to_guess}.')

# task_2
name = input('What is your name?')
age = input('How old are you?')
if age.isdigit():
    true_age = int(age)
    print(f"Hello {name}, on your next birthday you'll be {true_age + 1} and happy!")
else:
    print('Answer is not valid!')

# task_3
'''
Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)
'''
import random

generated_words = 0
word = input('Write 1 word please')

while generated_words < 5:
    generated_words += 1
    new_words = random.sample(word, len(word))
    print(''.join(new_words))


