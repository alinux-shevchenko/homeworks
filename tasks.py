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

