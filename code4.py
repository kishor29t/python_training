# Given number is even or odd
# num = int(input("Enter the number: "))
# for i in range(num):
#     print(i)
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# Sum of two numbers (throw error)
# a=int(input("enter the value1:"))        
# b=int(input("enter the value2:"))
# sum=a+b
# print("sum=",sum)
# try:
#     a = int(input("Enter value 1: "))
#     b = int(input("Enter value 2: "))
#     sum = a + b
#     print("Sum =", sum)
# except ValueError:
#     print("Error: Please enter valid integers only.")
# except Exception as e:
#     print("Unexpected error:", e)

# print("This is the last line.")

# Check whether number is positive, negative or zero
# num=int(input("enter the number:"))
# if num > 0:
#      print("positive number")
# elif num < 0:
#         print("negative number")
# else:
#             print("number is zero")

# Check the number entered is numeric or not
# num1 = input("Enter num 1: ")
# num2 = input("Enter num 2: ")

# if not num1.isnumeric():
#     print("num1 is not a number")
# elif not num2.isnumeric():
#     print("num2 is not a number")
# else:
#     res = int(num1) + int(num2)
#     print("Sum =", res)

# Handel the error (str)
# num=input("enter num 1:")
# num2=input("enter num 2:")

# if num.isnumeric()==False:
#     print("num is not number")
# elif num2.isnumeric()==False:
#     print("num2 is not number")
# else:
#     res = int(num)+int(num2)
#     print(str(res))        


# Arthematic Operation
# a=int(input("enter the number-01:"))
# b=int(input("enter the number-02:"))
# print("Addition:",a+b)
# print("Substraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)

# Largest of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# largest = max(a, b, c)
# print("The largest number is:", largest)

#COUNT CHARACTERS IN STRING
# text = "carrier"
# character_count = len(text)
# print("Number of characters:", character_count)

#COUNT CHARACTERS IN STRING-1
# text = "aabcdcdd"

# # Create an empty dictionary to store counts
# char_count = {}

# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# # Print the counts
# for char, count in char_count.items():
#     print(f"{char}: {count}")

#COUNT CHARACTERS IN STRING-2
# char_count = {}

# name = "hi how are you"

# for c in name:
#     if c not in char_count:
#         char_count[c] = 1 
#     else:
#         char_count[c] += 1  

# print(char_count) 

#Define the method
# def add():
#     print("this is add")
# #calling the method
# add()    

# name = "do you know who i am"
# num = 45
# print(name + str(num))

#CONCATINATION
# name="chan..."
# age=21;
# print(f"Name is {name} and his age is {age}.")
# text=f"Name is {name} and his age is .{age}"
# print(text)

#
# def print_user_info(name, city):
#     text = f"Name is {name} and his city is {city}."
#     print(text)


# print_user_info("Jonh()", "Bali")

#
# from datetime import datetime

# def print_datetime():
#     now = datetime.now()
#     print("Current date and time:", now)

# print_datetime()

# Calculate age
from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year

    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1

    return age


print("Age is:", calculate_age(2004, 11, 30))


