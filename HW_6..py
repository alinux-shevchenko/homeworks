# task_1
#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

sentence = input('Write any sentence, please!')
true_sentence = sentence.lower()
words = true_sentence.split()   #розбиваємо речення користувача на слова
word_count = {}

for word in words:
    if word in word_count:    #якщо слово вже є ключем в словнику
        word_count[word] += 1   #то значення зростає на 1
    else:
        word_count[word] = 1   #прописуємо, що для кожного 1го ключа значення 1


print(word_count)


# task_2
#Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.
# The code has to return the dictionary with the sums of the prices by the goods types.

#Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = 0
price_by_type = {}
for item in stock:
    total_price += stock[item] * prices[item]
    price_by_type[item] = stock[item] * prices[item]
print(price_by_type)
print(f"The total price is {total_price}.")

# task_3
#Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

tuplist = [(i, i**2) for i in range(1, 11)]
print(tuplist)

# task_4
#Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_dict_1 = {i+1: day for i, day in enumerate(days)}   #використовуємо enumerate() для отримання індексу кожного елемента
print(day_dict_1)

day_dict_2 = {day: i for i, day in day_dict_1.items()}   #використовуємо items() для отримання пар ключ-значення зі словника day_dict_1
print(day_dict_2)