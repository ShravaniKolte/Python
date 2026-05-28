#Program 7: Reverse a Number Using while Loop
print("Program to Reverse a Number Using while Loop")
number = int(input("Enter a number to reverse: "))  
reversed_number = 0
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = (reversed_number * 10) + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the original number
print(f"The reversed number is: {reversed_number}")
print("--------------------------------------")
print("Number reversed successfully")