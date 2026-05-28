#Print Even Numbers Using for Loop
print("Program to Print Even Numbers")
limit = int(input("Enter the limit up to which you want to print even numbers: "))
print(f"Even numbers up to {limit} are:")
for num in range(2, limit + 1, 2):
    print(num, end=' ')
print("\n--------------------------------------")
print("Even numbers printed successfully")