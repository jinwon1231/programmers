def solution(numbers, n):
    i = 0
    sum = 0
    while sum <= n:
        sum = sum + numbers[i]
        i = i + 1

    return sum