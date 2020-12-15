import os
#My first calculator 01/12/2020

#This is my first prototype and I will be updating on it.

#Things to include: 

#calculation combo
#exit options
#update if statements
#


def menu_message():
    print("""
    Welcome to my calculator, please select from following options:
    [1] Calculator
    [2] Exit Application
    """)

def menu_selection():
    in_put = int(input("Please select from the menu options by inputting a value: "))
    if in_put == int(1):
        calculator_options()
    elif in_put == int(2):
        print("Thank you for using calculator, closing...")

def general_input():
    int(input("Please enter your number: "))


def calculator_options():
    calc_input = str(input("Please type and press enter for type of calculation you wish to use e.g. + - * / exponent or exit to return to menu: "))
    if calc_input == "+":
        first_input = float(input("please enter your first number: "))
        second_input = float(input("please enter your second number: "))
        print(addition(first_input,second_input))
        input("Please press any key to return to menu")
        calculator_options()
    elif calc_input == "-":
        first_input = float(input("please enter your first number: "))
        second_input = float(input("please enter your second number: "))
        print(subtraction(first_input,second_input))
        input("Please press any key to return to menu")
        calculator_options()
    elif calc_input == "*":
        first_input = float(input("please enter your first number: "))
        second_input = float(input("please enter your second number: "))
        print(multiplication(first_input,second_input))
        input("Please press any key to return to menu")
        calculator_options()
    elif calc_input == "/":
        first_input = float(input("please enter your first number: "))
        second_input = float(input("please enter your second number: "))
        print(division(first_input,second_input))
        input("Please press any key to calculation options")
        calculator_options()
    elif calc_input == "exponent":
        exponent()
        input("Please press any key to return to menu")
        calculator_options()
    elif calc_input == "exit":
        clear_screen()
        menu_message()
        menu_selection()
    else: 
        print("None of which you have typed corresponds with the selection..")
        calculator_options()
    

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def division(a,b):
    return a / b

def multiplication(a,b):
    return a * b

def exponent():
    first_inp = float(input("Please enter the number you wish to use for this calculation: "))
    second_inp = float(input("Please enter the second number you would like to apply to the power of: "))
    apply_power = first_inp ** second_inp 
    print(apply_power)


def clear_screen():
    os.system("clear")

menu_message()
menu_selection()