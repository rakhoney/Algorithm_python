arr = [0, 1]


def solution(n):
    for i in range(n - 1):
        result = arr[0] + arr[1]
        arr.append(result)
        arr.pop(0)

    answer = arr[1]
        
    answer = answer % 1234567
    return answer

