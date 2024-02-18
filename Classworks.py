# Компьютер "загадую" число від 1 до 99 і пропонує користувачеві його відгадати з 10 спроб.
# Якщо користувач вгадав - програма завершується, вітає з перемогою і виводить "Congratulations! You've won in <N> attempts!" (де N - кількість спроб).
# Якщо число не вгадане, а спроби ще залишаються - комп'ютер повідомляє чи загаданге число більше, чи менше введеного.
# Якщо число не вгадане за всі десять спроб - комп'ютер виводить "Sorry, the number is <X>. Wanna try again?", де X - число, яке було загадане.
# * Якщо користувач вводить невалідне значення - комп'ютер не рахує цієї спроби та виводить "Please, enter a valid number in range [1..99]"
#Ось цей випадок треба додати, коли число менше 1 або більше 99

import random


def main(): #функція є точкою входу і задає базові параметри для використання.
    total_answers_count = 0
    is_guessed = False #ці змінні будуть використовуватися в подальшому коді і ми задаємо їм стартові параметри

    number_to_guess = random.randint(1, 99) #загадуємо число

    while total_answers_count < 10 and not is_guessed: #починаємо задавати кількість спроб, якщо спроб менше 10 (починаємо з 0), з кожною спробою ми додаємо 1 до кількості і так раху-ься кіл-ть спроб
        row_user_answer = input("Please guess the number in range [1..99]:\n") #промпт для юзера
        if row_user_answer.isdigit():
            total_answers_count += 1
            user_answer = int(row_user_answer) #тут і вище переводимо відповідь юзера в int зі str
            if number_to_guess == user_answer:
                is_guessed = True
                print(f"Congratulations! You've won in {total_answers_count} attempts!") # якщо відповідь юзера = рандомному числу, то виводимомо вітаня
            else:
                if number_to_guess > user_answer:
                    print(f"No exactly! The number is bigger than {user_answer}")
                else:
                    print(f"No exactly! The number is less than {user_answer}") # даємо підказки, якщо юзер не вгадав
        else:
            print("Please, enter a valid number in range [1..99]") # виводиться, коли юзер ввів текст, чи число поза числовим проміжком
        print(f"Sorry, the number is {number_to_guess}. Wanna try again?")


if __name__ == "__main__":
    main()