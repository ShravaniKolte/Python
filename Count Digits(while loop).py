#Program 8: Count Digits in a Number Using while Loop
print("Program to Count Digits in a Number Using while Loop")
number = int(input("Enter a number to count its digits: "))
count = 0
if number == 0:
    count = 1  # The number 0 has one digit
else:
    while number > 0:
        number //= 10  # Remove the last digit
        count += 1  # Increment the count for each digit removed
print(f"The number of digits in the entered number is: {count}")
print("--------------------------------------")
print("Digit count completed successfully")