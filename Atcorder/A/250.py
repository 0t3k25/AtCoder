if __name__ == "__main__":
    H, W = (int(x) for x in input().split())
    C, D = (int(x) for x in input().split())
    count = 0
    for a in range(1, H + 1):
        for b in range(1, W + 1):
            if abs(a - C) + abs(b - D) == 1:
                count += 1
    print(count)
