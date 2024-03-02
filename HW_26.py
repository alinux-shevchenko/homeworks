# task_1
#Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
# Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
# Визначте складність алгоритму та порівняйте його з бінарним пошуком

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# O(log n)

def fibonacci_search(arr, x):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    index = -1
    while fib > 1:
        i = min(index + fib2, (len(arr)-1))
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            index = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and index < (len(arr)-1) and arr[index+1] == x:
        return index+1
    return -1

# O(log n)