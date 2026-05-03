n = int(input("How many terms do you want in Fibonacci series? "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
