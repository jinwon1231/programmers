def solution(n):
    result = []
    for i in range(n):
        arr = [0] * n
        arr[i] = 1
        result.append(arr)
    return result