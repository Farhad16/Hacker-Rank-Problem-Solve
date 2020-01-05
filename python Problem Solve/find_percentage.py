if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    avg = 0
    for name, numbers in student_marks.items():
        if name == query_name:
            for number in numbers:
                avg += number
    print('%.2f' % (avg/3))
