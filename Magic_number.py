n = int(input("Enter a number: "))
while n > 9:
    s = 0
    while n > 0:
        s = s + (n % 10)
        n = n // 10
    n = s
if n == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")
