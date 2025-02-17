# Anthony Oliva
# 02/15/2025
# P1HW1
# This program collects user input, performs exponentiation, addition, and subtraction, and displays the results.

print("-----Calculating Exponents-----")


base= int(input("Enter an integer as the base value: "))
exponent= int(input("Enter an integer as the exponent: "))

result= base * exponent

print(base, "raised to the power of" , exponent, "is" , result, "!!")

print("------Addition and Subtraction----")

start_value= int(input("Enter a starting integer: "))
add_value= int(input("Enter a integer to add: "))
subtract_value= int(input("Enter a integer to subtract: "))

final_result= start_value + add_value - subtract_value

print(start_value, "+", add_value, "-" , subtract_value, "is equal to" , final_result)
