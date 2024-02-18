# task_1
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

import random

numbers_list = []
list_length = 0

while list_length < 10:
    numbers_list.append(random.randint(1,500))
    list_length +=1

print(numbers_list)
print(max(numbers_list))



# task_2

import random

numbers_list_1 = []
numbers_list_2 = []
list_length_1 = 0
list_length_2 = 0

while list_length_1 < 10:
    numbers_list_1.append(random.randint(1,10))
    list_length_1 +=1

while list_length_2 < 10:
    numbers_list_2.append(random.randint(1,10))
    list_length_2 +=1

common_numbers = set(numbers_list_1).intersection(set(numbers_list_2))

print(numbers_list_1)
print(numbers_list_2)
print(list(common_numbers))



# task_3

raw_list = list(range(1, 101))
fresh_list = []
iteration = 0

while iteration < len(raw_list):
    if raw_list[iteration] % 7 == 0 and raw_list[iteration] % 5 != 0:
        fresh_list.append(raw_list[iteration])
    iteration += 1

print(fresh_list)

