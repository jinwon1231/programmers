def solution(s):
    answer = 0
    a = 0
    b = 0
    s = s.lower()
    for i in s:
        if i == "p":
            a = a + 1
        elif i == "y":
            b = b + 1

    if a == b:
        answer = True
    else:
        answer = False

    return answer