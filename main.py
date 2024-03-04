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
