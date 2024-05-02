n = int(input())
i = 0

for _ in range(n):
    i += 1
    print((n-i) * " ", i * "*", sep='')
