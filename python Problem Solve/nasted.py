students = [['Harsh', 20], ['Beria', 20], [
    'Varun', 19], ['Kakunami', 19], ['Vikas', 21]]

numbers = []
for student in students:
    numbers.append(student[1])

unique = []
for i in sorted(numbers):
    if i not in unique:
        unique.append(i)

for name, marks in sorted(students):
    if marks == unique[1]:
        print(name)

# second_lowest_mark = sorted(list(dict.fromkeys(numbers)))
# print(second_lowest_mark)
