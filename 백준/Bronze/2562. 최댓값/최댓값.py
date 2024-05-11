# ## 풀이1.  인덱스 없이 직접 구현 
# # 값은 나오나 백준에서 오답처리 됨
# x = []
# for _ in range(9):
#     x.append(int(input()))

# max = x[0]
# cnt = 0
# cnt_max = 0
# for i in x:
#     cnt += 1
#     if i > max:
#         max = i
#         cnt_max = cnt

# print(max)
# print(cnt_max)

    
## 풀이2. 인덱스와 리스트컴프리헨션으로 구현

x = [int(input()) for _ in range(9)]

print(max(x))
print(x.index(max(x))+1)