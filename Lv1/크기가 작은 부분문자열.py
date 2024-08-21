def solution(t, p):
    answer = 0
    p1 = len(p)
    t1 = len(t)
    p = int(p)
    for i in range(0,t1+1-p1):
        if int(t[i:i+p1]) <= p:
            answer = answer + 1
    return answer