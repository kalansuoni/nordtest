try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 + number2
    print(f"The sum is {result}.")

except ValueError:
    print("Sorry, you must enter numbers only.")