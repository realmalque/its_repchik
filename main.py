# def main():
#     height = get_height()
#     for i in range(height):
#         print('#')

# def get_height():
#     while True:
#         try: 
#             n = int(input("Height="))
#             if n > 0:
#                 return n
#         except ValueError:
#             print('Enter the number!')
# main()

# score = [72,73,33]
# avarage = sum(score)/len(score)
# print(f'Avarage = {avarage}')

# scores = []
# for i in range(3):
#     score = int(input("Score: "))
#     scores += [score]

# avarage = sum(scores)/len(scores)
# print(f"Avarage: {avarage}")

# before = input('Before:')
# after = before.upper()
# print(f'After: {after}')

# import sys

# names = ['Bill', 'Petro', 'Vova', 'Kolya', 'Masha', 'Luda', 'Sveta']
# name = input("name:")
# if name in names:
#         print("found")
#         sys.exit(0)

# print('not found')
# sys.exit(1)

# spisok = [1,2,3,5,7,3, 4, 3,4, 3]
# spisok.append(13)
# spisok[0] = 90
# spisok.pop(1)
# pisok = ['pis','ok','banana', 'casemiro', 'donald duck', 'like', 'ant']
# spisok.extend(pisok)
# sorted_pisok = sorted(pisok, key=len, reverse= True)
# print(sorted_pisok, pisok)
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# print(my_dict["name"])  # Виведе 'Alice'
# my_dict["age"] = 26  # Змінює вік на 26
# my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
# del my_dict['age']
# name = my_dict.pop("name")
# gender = my_dict.get("gender")
# print('name' in my_dict)
# print ('age' in my_dict)

# a = {1, 2, 3}
# b = {3, 4, 5}
# # print(a.intersection(b))  # {3}
# print(a ^ b)  # {3}
# print(b.symmetric_difference(a))
# print(a.union(b))
# print(a|b)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[::2]
# print(odd_numbers)
# even_numbers = numbers[1::2]
# print(even_numbers)

# cat = {}
# info = {"status": "vaccinated", "breed": True}
# cat['nick'] = 'Simon'
# cat["age"] = 7
# cat["characteristics"] = ["лагідний", "кусається"]
# age = cat.get("age")
# cat.update(info)
# pri

# num = int(input("Enter a number: "))
# if num > 0:
#     if num // 2 == 0
#         result = "Positive even number" 
#     else:
#         result = "Positive odd number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))
    
# result = y / x

# is_nice = False
# state = "nice" if is_nice else "not nice"
# print(state)
fruit = "tukva"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

# point = (0, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")

# fruit = 'apple'
# for char in fruit:
#     print(char, end="")

# start_string = input("Enter your string:")
# total_length = len(start_string)
# counter = 0
# for i in start_string:
#     if i == " ":
#         counter += 1
# print(f"Total spaces equals {counter}")
# print(f"Total length equals {total_length}")

# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

# my_list = [2, 3, 4, 5]
# product = 1
# for num in my_list:
#     product *= num
# print(product)

# num = 5
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1
# print(factorial)

# for num in range(2, 51):
#     for i in range(2, num):
#         if not num % i :
#             break
#     else:
#         print(num)

# for num in range(1, 21):
#     if not num % 3 or not num % 5:
#         print(num)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num>0:
#     sum += num
#     num -=1
    
# print(sum)

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }
# for key, val in numbers.items():
#     print(key, val)

# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#      print(f"val {val} is not a number")
# # else:
# #     print(val > 0)
# finally:
#       print("This will be printed anyway")
# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")


# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# def modify_list(lst: list) -> None:
#     lst = my_list
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]
# print(modify_list(lst=[3,5]))

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes
# result = string_to_codes("Hello world!")
# print(result)

# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)


# func(1, 1, 1)

# def get_fullname(first_name, last_name, middle_name = ""):
#     if middle_name == "":
#         print(f'{first_name} {last_name}')
#     else:
#         print(f'{first_name} {middle_name} {last_name}  ')
# get_fullname("Petro", "Voloshyn", "Ivanovych")

# def get_fullname(first_name, last_name, middle_name =""):
#     if middle_name:
#         print(f"{first_name} {middle_name} {last_name}")
#     else:
#         print(f"{first_name} {last_name}")
# get_fullname("Vasyl","Ivanov","Petrovich")

# def get_fullname(first_name, last_name, middle_name = None):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name
# first_name = "Іван"
# last_name = "Петров"
# middle_name = "Олександрович"

# result = get_fullname(first_name, last_name, middle_name)
# print(result)

def format_string(string:str, length:int):
    if len(string) >= length:
        line = string
    elif len(string) < length:
        line = " " * ((length-len(string))//2) + string
    return line
format_string ('Hello to everyone', 35)
    