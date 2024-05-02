t = int(input())
k = 1

for _ in range(t):
    a, b = map(int, input().split())
    c = a + b
    print("Case #", k, ": ", a, " + ", b, ' = ', c, sep='')

    k += 1