#!/usr/bin/env python3
  
def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(e)
       
def calculator():
    operators = ['+', "-", "/", "*"]
    numbers = (0,1,2,3,4,5,6,7,8,9)
    
    operator = input("Please choose an operator. Valid operators are +, -, /, * : ")
    
    if operator in operators:
        num1 = int(input("Enter any number between 0-9: "))
        num2 = int(input("Enter any number between 0-9: "))
        
        if num1 in numbers and num2 in numbers:
            if operator == '+':
                print( num1, '+' , num2, '=' , sum(num1, num2))
        
            elif operator == '-':
                print(num1, "-", num2, "=", subtract(num1, num2))
        
            elif operator == '*':
                print(num1, "*", num2, "=", multiply(num1, num2))
        
            elif operator == '/':
                print(num1, "/", num2, "=", divide(num1, num2))
                
            else:
                print("Please enter a valid number")
        
        else:
            print("Please input valid number.")
    else:
         print("Invalid input. Please select valid operator.")
         calculateAgain()

def calculateAgain():
    calculate_again = input("Would you like to calculate again? Please enter 'Y' or 'N'")

    if calculate_again.lower() == 'y':
        calculator()
    elif calculate_again.lower == 'n':
        print("You have a good day!")
    else:
        calculateAgain()

calculator()
calculateAgain()
