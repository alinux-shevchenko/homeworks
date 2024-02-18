# task_1
#Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {args}")
        return func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(4,5))
print(square_all(4,5))

# task_2
#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# task_3
#Write a decorator "arg_rules" that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Error: Argument {arg} is not of type {type_}")
                    return False
                if len(arg) > max_length:
                    print(f"Error: Argument {arg} exceeds maximum length of {max_length}")
                    return False
                if not all(symbol in arg for symbol in contains):
                    print(f"Error: Argument {arg} does not contain all symbols {contains}")
                    return False
            return func(*args, **kwargs)
        return wrapper

    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'