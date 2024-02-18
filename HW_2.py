#task_1
name = 'Alina'
day = 'Sunday'

print(f'Good day {name}! {day} is a perfect day to learn some python.')

s = 'Good day {}! {} is a perfect day to learn some python.'
print(s.format(name, day))

print('Good day {1}! {0} is a perfect day to learn some python.'.format(day,name))

print('Good day %s! %s is a perfect day to learn some python.' %(name, day))

#task_2
first_name = 'Alina'
last_name = 'Shevchenko'
first_name, last_name = 'Alina', 'Shevchenko'
name = first_name + ' ' + last_name
day = 'Sunday'
print(f'Good day {name}! {day} is a perfect day to learn some python.')

#task_3
a = 11
b = 99
print(a+b)
print(b-a)
print(b/a)
print(a*b)
print(b**a)
print(a//b)