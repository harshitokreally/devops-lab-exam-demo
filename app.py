def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

try:
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input. Please enter an integer.")
