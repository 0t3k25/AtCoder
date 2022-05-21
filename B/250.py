if __name__ == "__main__":
    N, A, B = map(int, input().split())
    line_1, line_2 = "", ""
    marks = [".", "#"]
    mark = marks[0]
    for i in range(N):
        line_1 = line_1 + mark * B
        if mark == ".":
            mark = "#"
        else:
            mark = "."
        line_2 = line_2 + mark * B
    for i in range(N):
        line = line_1 if i % 2 == 0 else line_2
        for i in range(A):
            print(line)
