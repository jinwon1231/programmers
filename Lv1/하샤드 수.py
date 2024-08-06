def solution(x):
    answer = 0
    for i in str(x):
        answer = answer + int(i)
    if int(x) % answer == 0:
        return True
    else:
        return False
