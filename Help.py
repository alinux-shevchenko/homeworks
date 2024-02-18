# Title
a = 'abba'
b = 'baab'
print(a.title() + ' ' + b.title())

# ЗРІЗ
name = 'Alina Shevchenko'
initials = name[0] + name[6]
print(name[0:6] + initials + ' ' + name[6:len(name)])

# IF
weather = 'cloudy'
if weather == 'sunny':
    print('Today is zaebis')
elif weather == 'rainy':
    print('Today is huevo')
else:
    print('Myamyamya')

# AND/OR/NOT
# 2 and - true тільки якщо всі true
# 3 or - false тільки якщо всі умови хибні
# 1 not - якщо not true, тл поверне false

# WHILE
myska = 1000
sour_cream = 0

while sour_cream < myska:
    print(f'sour_cream : {sour_cream}', end=' ')
    print('add more')
    sour_cream += 1
    #збільшили сметану на 1
    if sour_cream %7 ==0:
        #%7 тут покаже залишок ділення сметани на 7
        print('it is fine, stop')
        break

was = 23
take = 1

while take < was:
    print (f'smetana : {take}.', end=' ')
    if take % 7 == 0:
        print('add one more')
        take += 1
        continue
    print('xxxxx')
    take += 1

# INPUT
variable1 = input('write a number')
if variable1.isdigit():
    print(int(variable1)+10)
else:
    print('Invalid number')


