# David Sanchez
# CIT-95-30164-2024FA
# PythonFall24Module01
# Write a Python program that uses nested if statements (nested decisions) to get three
# integers from the user and outputs the largest of the three. Name your source code file: "largestOfThree.py"


# Input will attempt to convert to int. If input from user cannot be converted, error message will be displayed and request will be repeated.
def verify_input(user_input):
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("Please input a number! ")
# Function to find the largest int and return the largest int
def find_largest_num(first_num, second_num, third_num):
    l_num = first_num
    if second_num > l_num:
        largest = second_num
    if third_num > l_num:
        l_num = third_num
    return l_num
#Request input from user and call verify_input to convert / verify input
num1 = verify_input("Enter the first number: ")
num2 = verify_input("Enter the second number: ")
num3 = verify_input("Enter the third number: ")

#largest number returned from function and stored in largest_num variable
largest_num = find_largest_num(num1, num2, num3)
#largest number printed.
print("The largest number you entered was:", largest_num)