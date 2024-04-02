from collections import deque

def solution(arr):
    dq = deque(arr)  
    answer = []
    
    if dq:  
        answer.append(dq.popleft())  
    
    for i in dq:  
        if answer[-1] != i:  
            answer.append(i)

    return answer

# from collections import deque

# a = list(map(int, input().split(',')))

# def solution(arr):
    
#     dq = deque(a)
#     answer = []
#     answer.append(dq[0])
#     dq.popleft()
    
#     for i in a:
#         if answer[-1] == i:
#             pass
#         elif answer[-1] != i:
#             answer.append(i)
#     print(answer)
    
#     return answer





