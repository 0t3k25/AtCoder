H, W = (int(x) for x in input().split())
R, C = (int(x) for x in input().split())


next_count = 0
# 上
up_R = R - 1
if 1 <= up_R < H:
    next_count += 1

# 下
down_R = R + 1
if 1 < down_R <= H:
    next_count += 1

# 左
left_C = C - 1
if 1 <= left_C < W:
    next_count += 1


right_C = C + 1
if 1 < right_C <= W:
    next_count += 1


print(next_count)
