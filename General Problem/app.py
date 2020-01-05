def plusMinus(arr):
    positive = 0
    negative = 0
    zeroc = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
            print("positive", i)
        elif arr[i] < 0:
            negative += 1
            print("negative", i)

        elif arr[i] == 0:
            zeroc += 1
            print("zero", i)

    print(positive / len(arr))
    print(negative / len(arr))
    print(zeroc / len(arr))


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
