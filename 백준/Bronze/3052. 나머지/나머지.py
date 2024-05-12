## 1. set함수로 풀기
num = []
for _ in range(10):
    num.append(int(input())%42)

anw = set(num)
print(len(anw))

# ## 2. for문으로 풀기
# num = []
# for _ in range(10):
#     a = int(input())
#     if a%42 not in num:
#         num.append(a%42)
# print(len(num))