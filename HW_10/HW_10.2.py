# task_2

#The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application, else raise an error.
# After the user exits, all data should be saved to loaded JSON.

'''
Add new entries +
Search by first name+
Search by last name+
Search by full name+
Search by telephone number+
Search by city or state+
Delete a record for a given telephone number +
Update a record for a given telephone number +
An option to exit the program

'''
import json

contact = {
    'first_name': 'Pes',
    'last_name':'Patron',
    'full_name': 'Pes Sobaka Patron',
    'phone_number':'+380677777777',
    'city':'Kyiv',
}
contacts = {
    '+380677777777':{
        'first_name': 'Pes',
        'last_name':'Patron',
        'full_name': 'Pes Sobaka Patron',
        'phone_number':'+380677777777',
        'city':'Kyiv',
    },
}


#========= contact / base funcs =========


def add_contact(contact: dict):
    key = contact['phone_number']
    contacts[key] = contact


def delete_contact(phone_number: str):
    if phone_number in contacts:
        del contacts[phone_number]


def update_contact(phone_number: str, new_contact: dict):   # код копілота, трохи заплуталась і не впевнена що це працює так, як задумувалось
    if phone_number in contacts:
        contacts[phone_number] = new_contact
import json

def update_contact():
    with open('contacts.json') as f:
        contacts = json.load(f)
    phone_number = input('Write phone number! ')
    if phone_number not in contacts:
        print('Phone number is not found!')
        return
    new_contact = {}
    new_contact["name"] = input("Введіть ім'я: ")
    new_contact["email"] = input("Введіть електронну адресу: ")
    new_contact["address"] = input("Введіть адресу: ")
    update_contact(phone_number, new_contact)
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)


def save(path: str):
    with open(path, 'w') as contact_file:
        contact_file.write(json.dumps(contacts))


# ========= search funcs =========


def search_by_first_name(first_name: str):
    results = []
    for key, value in contacts.items():
        if value['first_name'] == first_name:
            results.append(value)
    return results


def search_by_last_name(last_name: str):
    results = []
    for key, value in contacts.items():
        if value['last_name'] == last_name:
            results.append(value)
    return results


def search_by_full_name(full_name: str):
    results = []
    for key, value in contacts.items():
        if value['full_name'] == full_name:
            results.append(value)
    return results


def search_by_phone_number(phone_number: str):
    results = []
    for key, value in contacts.items():
        if value['phone_number'] == phone_number:
            results.append(value)
    return results


def search_by_city(city: str):
    results = []
    for key, value in contacts.items():
        if value['city'] == city:
            results.append(value)
    return results


#========= user input funcs =========


def read_first_name():
    while True:
        first_name = input('Write first name! ')
        if first_name.isalpha():
            return first_name.capitalize()
        else:
            print("Please enter a valid name with only letters.")


def read_last_name():
    while True:
        last_name = input('Write last name! ')
        if last_name.isalpha():
            return last_name.capitalize()
        else:
            print("Please enter a valid last name with only letters.")


def read_full_name():
    while True:
        full_name = input('Write full name! ')
        if all(char.isalpha() or char.isspace() for char in full_name):
            return full_name.title()
        else:
            print("Please enter a valid full name with only letters and spaces.")


def read_phone_number():
    while True:
        phone_number = input('Write phone number! ')
        if phone_number.startswith('+') and phone_number[1:].isdigit():
            return phone_number
        else:
            print("Please enter a valid phone number starting with '+' and containing only digits.")


def read_city():
    while True:
        city = input('Write city! ')
        if city.isalpha():
            return city.capitalize()
        else:
            print("Please enter a valid city with only letters.")


def read_contact():
    return {
        'first_name': read_first_name(),
        'last_name': read_last_name(),
        'full_name': read_full_name(),
        'phone_number': read_phone_number(),
        'city': read_city(),
    }


#========= user input search funcs =========





#========= user input operation funcs =========


def read_operation():
    operation = input('>>> ')

    return operation


def read_filepath():
    while True:
        path = input('Please, write the name of your phonebook file in .json format: ')
        if path.endswith('.json'):
            return path
        else:
            print('Invalid file name. Please enter a valid file name in JSON format.')


def add_handler(filepath: str):
    contact = read_contact()
    add_contact(contact)
    save(filepath)
    print('Contact added successfully')


#========= main.py =========


def main():
    filepath = read_filepath()
    while True:
        print(
            'write "create" to add new contact' + '\n'                                    #+
            'write "search_f_name" to search by first name' + '\n'
            'write "search_l_name" to search by last name' + '\n'
            'write "search_name" to search by full name' + '\n'
            'write "search_phone" to search by phone number' + '\n'
            'write "search_city" to search by city' + '\n'
            'write "del" to delete a record for a given telephone number' + '\n'
            'write "update" to update a record for a given telephone number' + '\n'
            'write "exit" to exit'                                                     #+
        )

        operation = read_operation()

        if operation in ('a', 'add', 'add_contact'):
            add_handler(filepath)
        elif operation in ('search_f_name'):
            ...
        elif operation in ('e', 'exit'):
            break
        else:
            print(f"!!! Invalid operation `{operation}` !!!")


if __name__ == '__main__':
    main()