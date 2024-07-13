def solution(n):
    answer = 0
    for i in range(n):
        if ((i+1)*6) %n == 0:
            answer = answer + i+1
            break
    return answer