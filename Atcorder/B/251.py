N, W = map(int, input().split())
A = list(map(int, input().split()))

count = [0] * (W + 1)

for i in A:
    if i <= W:
        count[i] = 1

for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            count[A[i] + A[j]] = 1

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                count[A[i] + A[j] + A[k]] = 1

print(sum(count))
