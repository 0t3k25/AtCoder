N = int(input())

score = dict()
PP = [-1, -1]
for i in range(1, N + 1):
    si, ti = input().split()
    ti = int(ti)
    if si not in score:
        score[si] = ti
        if PP[0] < ti:
            PP = [ti, i]
print(PP[1])
