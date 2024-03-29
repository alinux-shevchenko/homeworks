# task_1
#Write a Python program to detect the number of local variables declared in a function.

def count_local_variables(func):
    return func.__code__.co_nlocals

def my_function():
    x = 1
    y = 2
    z = 3
    print(count_local_variables(my_function))

my_function()

# task_2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def hours_day(a):
    def days_week(b):
        return a * b
    return days_week

hours_week = hours_day(24)
print(hours_week(7))

# task_3
#Write a function called "choose_func" which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))