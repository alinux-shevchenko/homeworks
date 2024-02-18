# task_1
#Create a class method named `validate`, which should be called from the
# `__init__` method to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

import re
from email_validator import validate_email, EmailNotValidError

class User:
    def __init__(self, email):
        self.email = self.validate(email)

    def validate(self, email):

        try:
            # Validate the email using email-validator
            valid_email = validate_email(email)
            return valid_email.email
        except EmailNotValidError:
            raise ValueError("Invalid email address")

# Example usage
try:
    user = User("example@email.com")
    print(f"Valid email: {user.email}")
except ValueError as e:
    print(f"Error: {e}")

# task_2
#Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list
# directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.

#id_ - is just a random unique integer

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

