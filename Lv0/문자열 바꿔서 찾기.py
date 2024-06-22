def solution(myString, pat):
    answer = 0
    a = ''
    for i in myString:
        if i == "A":
            a = a + "B"
        else:
            a = a + "A"
    if pat in a:
        answer = 1
    else:
        answer = 0

    return answer 