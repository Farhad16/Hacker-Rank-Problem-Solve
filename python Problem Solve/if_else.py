n = int(input())
if n % 2 == 0:
    if (n >= 2 and n < 6) or n > 20:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
else:
    print("Weird")
