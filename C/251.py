N = int(input())
ST = [map(str, input().split()) for _ in range(N)]
S, T = [list(i) for i in zip(*ST)]
letter_list = list(set(S))
T_number = [int(T[S.index(i)]) for i in letter_list]
T_index = [int(S.index(i)) for i in letter_list]
max_index = [i for i, x in enumerate(T_number) if x == max(T_number)]
print(min([int(T_index[i]) for i in max_index]) + 1)
