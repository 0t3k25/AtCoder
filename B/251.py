N, W = map(int, input().split())
A = list(map(int, input().split()))
arr_n = A
count = 0
i = 0
j = 1
k = 2
while i < N - 1:
    arr_n.append(A[i] + A[j])
    j += 1
    if j > N - 1:
        i += 1
        j = i + 1
i = 0
j = 1
k = 2
while i < N - 2:
    arr_n.append(A[i] + A[j] + A[k])
    j += 1
    k += 1
    if k > N - 1:
        i += 1
        j = i + 1
        k = j + 1

arr_n = list(set(arr_n))
for i in arr_n:
    if W >= i:
        count += 1
print(count)
