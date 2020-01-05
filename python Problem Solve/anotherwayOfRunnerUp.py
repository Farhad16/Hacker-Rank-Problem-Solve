arr = [2, 3, 6, 6, 5]
arr.sort()
newList = []
for i in arr:
    if i not in newList:
        newList.append(i)

newList.sort(reverse=True)
print(newList[1])
