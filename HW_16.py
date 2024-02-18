# task_1
#Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class Student (Person):
    def __init__(self, firstname, lastname, age, grade, performance):
        super().__init__(firstname, lastname, age)
        self.grade = grade
        self.performance = performance

class Teacher (Person):
    def __init__(self, firstname, lastname, age, salary, subject, years_of_experience):
        super().__init__(firstname, lastname, age)
        self.salary = salary
        self.subject = subject
        self.years_of_experience = years_of_experience

# task_2
#Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    def square_nums(self, nums):
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        return [num for num in nums
                if num <=0]

    def filter_leaps(self, dates):
        return [date for date in dates
                if date % 4 == 0
                and (date % 100 != 0
                or date % 400 == 0)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# task_3
#Write a class Product that has three attributes:
# type
#name
#price
#Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

#Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.

#Also, the ProductStore class must have the following methods:

#add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)

#set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name).
# The discount must be specified in percentage

#sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error.
# It also increments income if the sell_product method succeeds.

#get_income() - returns amount of many earned by ProductStore instance.
#get_all_products() - returns information about all available products in the store.
#get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid amount")
        product.price *= 1.3  # Add a 30% price premium for your store
        self.products.append((product, amount))

    def set_discount(self, identifier, percent, identifier_type= 'name'):
        if identifier_type not in ['name', 'type']:
            raise ValueError("Invalid identifier type")
        if not isinstance(percent, int) or percent < 0 or percent > 100:
            raise ValueError("Invalid discount percentage")
        for product, amount in self.products:
            if identifier_type == 'name' and product.name == identifier:
                product.price *= (100 - percent) / 100
            elif identifier_type == 'type' and product.type == identifier:
                product.price *= (100 - percent) / 100

    def sell_product(self, product_name, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid amount")
        for i, (product, stock) in enumerate(self.products):
            if product.name == product_name:
                if stock < amount:
                    raise ValueError("Insufficient stock")
                self.products[i] = (product, stock - amount)
                self.income += product.price * amount  # Increment income
                return
        raise ValueError("Product not found")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product.type, product.name, product.price, amount)
                for product, amount in self.products]

    def get_product_info(self, product_name):
        for product, amount in self.products:
            if product.name == product_name:
                return (product.name, amount)
        raise ValueError("Product not found")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

# task_4
#Create your custom exception named 'CustomException',
# you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named 'logs.txt'.
# Tips: Use __init__ method to extend functionality for saving messages to file

import logging        #written by AI, I didn't get the logging

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        logging.basicConfig(filename='logs.txt', level=logging.ERROR)
        logging.error(msg)
