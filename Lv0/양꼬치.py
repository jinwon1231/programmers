def solution(n, k):
    answer = 0
    n = int(n)
    k = int(k)
    if int(n) >= 10:
        answer = n * 12000 + k * 2000 - 2000
    else:
        answer = n * 12000 + k * 2000

    return answer