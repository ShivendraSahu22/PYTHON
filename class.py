count = 0
n = int(input("Enter the number: "))
while n >1:
    if n % 2 == 0:
        n = n - 1
    elif n % 2 == 0:
        n = n / 2
    else:
        n = n /3
    count += 1
print("Number of steps: ", count)
