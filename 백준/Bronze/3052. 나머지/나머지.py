num = []
for _ in range(10):
    num.append(int(input())%42)

anw = set(num)
print(len(anw))