n = int(input())
arr = list(map(int, input().split()))

# maximumScore = max(arr)
# for i in arr:
#     if maximumScore == max(arr):
#         arr.remove(max(arr))
#         runner = max(arr)
# print(runner)

maxSc = 0
runnerUp = 0
for i in arr:
    if i > maxSc:
        maxSc = i
for i in arr:
    if i < maxSc:
        runnerUp = i
print(runnerUp)
