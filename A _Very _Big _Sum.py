def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i
    print(sum)


x = int(input())
ar = []
for number in range(x):
    ar = list(map(int, input().rstrip().split()))

aVeryBigSum(ar)
