n = int(input("Enter any number to find the factorial: "))
fact = 1
i = n
while i >= 1:
    fact = fact * i
    i -= 1
print(f"Factorial of number {n} is: {fact}")
