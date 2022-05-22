if __name__ == "__main__":
    N, Q = map(int, input().split())
    # N個のボールを並べる
    balls = [i + 1 for i in range(N)]

    balls_dict = dict(zip([i + 1 for i in range(N)], [i for i in range(N)]))
    print(balls_dict)
    adjacemt_Xi = 0
    for i in range(Q):
        # Xiは入れ替える値
        Xi = int(input())
        # Xi_indexは値の目印
        Xi_index = balls_dict[Xi]
        if Xi_index == N - 1:
            adjacemt_Xi = Xi_index - 1
        else:
            adjacemt_Xi = Xi_index + 1
        tmp = balls[adjacemt_Xi]
        print(*balls)
        balls[adjacemt_Xi] = Xi
        print(*balls)
        balls[Xi_index] = tmp
        balls_dict[Xi] = adjacemt_Xi
        balls_dict[tmp] = Xi_index
        print(balls_dict)
        print(*balls)
