def solution(num_list):
    answer = 0
    a = 1
    b = 0
    for i in num_list:
        a = a * i
        b = b + i
    if a < b*b:
        answer = 1
    else:
        answer=  0
    return answer