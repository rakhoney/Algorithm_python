n, m = map(int, input().split())

basket = [k+1 for k in range(n)]

for x in range(m):
    i, j = map(int, input().split())

    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for y in basket:
    print(y , end=' ')


