# task_1
#Make a class called Person.
# Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old.")

person1 = Person("Carl", "Johnson", 26)
person1.talk()

# task_2
#Create a class Dog with class attribute 'age_factor' equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

dog1 = Dog(5)
print(f"The dog's age in human equivalent is {dog1.human_age()} years.")

# task_3
#Create a simple prototype of a TV controller in Python.
#The default channel turned on before all commands is №1.
'''
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.


CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    pass

controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.exists(4) == "No"

controller.exists("BBC") == "Yes"
'''

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, N):
        self.current_channel_index = N - 1
        return self.channels[self.current_channel_index]

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def exists(self, N_or_name):
        if isinstance(N_or_name, int):
            return "Yes" if 1 <= N_or_name <= len(self.channels) else "No"
        else:
            return "Yes" if N_or_name in self.channels else "No"

'''
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())  # Output: BBC
print(controller.last_channel())  # Output: TV1000
print(controller.turn_channel(1))  # Output: BBC
print(controller.next_channel())  # Output: Discovery
print(controller.previous_channel())  # Output: BBC
print(controller.current_channel())  # Output: BBC
print(controller.exists(4))  # Output: No
print(controller.exists("BBC"))  # Output: Yes
'''
