#min()

def minfunc(args):
    if len(args) == 1:
        args = args[0]
    min_value = args[0]
    for value in args:
        if value < min_value:
            min_value = value
    return min_value

#len()

def lenfunc(somelist):
    i = 0
    for arg in somelist:
        i += 1
    return i

#in()

def in_func(value, somelist):
    for item in somelist:
        if item == value:
            return True
    return False

#sort()

#________________________________________________

def question1 is #3
def question2 is #5
def question3 is #2
def question4 is #6
def question5 is #4
def question6 is #1