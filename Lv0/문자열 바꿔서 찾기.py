def solution(myString, pat):
    answer = 0
    a=''
    for i in myString:
        if i=="A":
            a+="B"
        else:
            a+="A"
    if pat in a:
        return 1
    else:
        return 0