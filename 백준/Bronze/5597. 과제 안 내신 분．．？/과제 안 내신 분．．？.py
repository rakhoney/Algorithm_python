attend = [0] * 30
cnt = 0

for _ in range(28):
    x = int(input())
    attend[x-1] = x

for j in attend:
    cnt += 1
    if j == 0:
        print(cnt)