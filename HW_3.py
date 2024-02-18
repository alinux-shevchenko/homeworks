#task_1
sample1 = 'helloworld'
if len(sample1) >= 2:
    print(sample1[0:2]+sample1[-2:])
elif len(sample1) < 2:
    print('')

sample2 = 'my'
if len(sample2) >= 2:
    print(sample2[0:2]+sample2[-2:])
elif len(sample2) < 2:
    print('')

sample3 = 'x'
if len(sample3) >= 2:
    print(sample3[0:2]+sample3[-2:])
elif len(sample3) < 2:
    print('')

#task_2
ph_number = '1234556789'
if ph_number.isdigit() == True and len(ph_number) == 10:
    print('Correct!')
elif not ph_number.isdigit():
    print('Only digits!')
elif len(ph_number) != 10:
    print('Invalid number of digits!')

#task_3
question = 118-73
answer = input('Please write the answer for 118-73')
if answer.isdigit():
    true_answer = int(answer)
else:
    print('Answer is not valid!')
    true_answer = None
if true_answer == question:
    print('Correct!')
elif true_answer != question:
    print('Incorrect!')

#task_4

name = 'alina'
user_name = input('What is your name?')
if user_name.lower() == name:
    print(True)
else:
    print(False)