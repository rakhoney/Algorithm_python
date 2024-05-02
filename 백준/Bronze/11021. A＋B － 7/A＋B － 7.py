t = int(input())
k=0
for _ in range(t):
    k += 1
    a, b = map(int, input().split())
    c = a + b
    print("Case #" + str(k) + ": "  + str(c))