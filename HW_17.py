# task_1
#Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance
# of a Cat or Dog classes and performs talk method on input parameter

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("meow")

def animal_talk(animal: Animal):
    animal.talk()

dog = Dog()
cat = Cat()

animal_talk(dog)
animal_talk(cat)

# task_2
#Write a class structure that implements a library. Classes:

#1) Library - name, books = [], authors = []
#2) Book - name, year, author (author must be an instance of Author class)
#3) Author - name, country, birthday, books = []

#Library class

#Methods:

#- new_book(name: str, year: int, author: Author)
# - returns an instance of Book class and adds the book to the books list for the current library.
#- group_by_author(author: Author) - returns a list of all books grouped by the specified author
#- group_by_year(year: int) - returns a list of all the books grouped by the specified year

#All 3 classes must have a readable __repr__ and __str__ methods.
#Also, the book class should have a class variable which holds the amount of all existing books

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

        # - returns an instance of Book class and adds the book to the books list for the current library.

    def group_by_author(self, author):
        return [book for book in self.books
                if book.author == author]

        #- returns a list of all books grouped by the specified author

    def group_by_year(self, year: int):
        return [book for book in self.books
                if book.year == year]

        #- returns a list of all the books grouped by the specified year

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    total_books = 0  # variable to keep track of all existing books

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)  # Add book to the author's list
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"'{self.name}' ({self.year}) by {self.author}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country})"

    def __str__(self):
        return f"{self.name} ({self.country})"

# task_3
#Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів
# (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator)   # 3/4+4/5 = 3*5+4*4/(4*5) = 15/20+16/20 = 31/20

    def __sub__(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator)    # 3/4-4/5 = 3*5-4*4/(4*5) = 15/20-16/20 = -1/20

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)       #(3/4)*(4/5) = (3*4)/(4*5) = 12/20

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)      # (3/4)/(4/5) = (3*5)/(4*4) = 15/16

    def __eq__(self, other):
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __lt__(self, other):
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __gt__(self, other):
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

    def __ge__(self, other):
        return (self.numerator * other.denominator) >= (other.numerator * self.denominator)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
    