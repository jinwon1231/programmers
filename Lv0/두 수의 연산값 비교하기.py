def solution(a, b):
    answer = 0
    x = int(str(a) + str(b))
    y = 2 * int(a) * int(b)
    if x >= y:
        answer = x
    else:
        answer = y

    return answer