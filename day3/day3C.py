#!/usr/bin/env python3

def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():
    operator = input("Please choose an operator. Valid operators are +, -, /, *.")
    operators = ['+', "-", "/", "*"]

    num1 = int(input("Enter any number between 0-9: "))
    num2 = int(input("Enter any number between 0-9: "))
   # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if operator == '+':
        print( num1, '+' , num2, '=' , sum(num1, num2))
        
    elif operator == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif operator == '*':
        print(num1, "*", num2, "=", multiply(num1, num2
