def solution(arr):
    answer = 0
    avg = 0
    for i in range(len(arr)):
        answer = answer + arr[i]
        avg = answer / len(arr)
    return avg