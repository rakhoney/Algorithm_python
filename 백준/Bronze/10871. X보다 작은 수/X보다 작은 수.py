n, x = map(int, input().split())

answer = []

a = list(map(int, input().split()))

for i in a:
    if i < x:
        answer.append(i)


print(*answer)
    
#### 잘못된 풀이
# n, x = map(int, input().split())

# answer = []

# for _ in range(n):
#     a = int(input())

#     if x > a :
#         answer.append(a)

# print(*answer)



