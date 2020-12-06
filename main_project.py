import os
#My first calculator 01/12/2020

#This is my first prototype and I will be updating on it.

#Things to include: 


def menu_message():
    print("""
    Welcome to my calculator, please select from following options:
    [1] Calculator
    [2] Exit Application
    """)

def calculator_message():
    print("""
    Please Enter your first number: 
    """)
    first_input()
    calculator_options()

def first_input():
    return first_input = float(input("Enter number here: "))

def calculator_options():
    calc_input = str(input("Please type and press enter for type of calculation you wish to use e.g. +,-,*,/: "))
    if calc_input = "+":
        addition()
    elif calc_input = "-":
        subtraction()
    elif 

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def division(a,b):
    return a / b

def multiplication(a,b):
    return a * b

def exponent():
    first_input()
    second_inp = input("Please enter the number you would like to apply to the power of: ")
    apply_power = first_input() ** second_inp 
    print(apply_power)

def menu_selection():
    in_put = input("Please select from the menu options by inputting a value: ")
    if in_put = int(1):
        print(calculator_message())
    else in_put = int(6):
        print("Thank you for using calculator, closing...")
    



def clear_screen():
    os.system("clear")