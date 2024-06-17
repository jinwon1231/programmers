def solution(num_list):
    a = 1
    b = 0
    answer = 0
    for i in num_list:
        a = int(i) * a

    for i in num_list:
        b = b + int(i)
    if int(a) < int(b) ** 2:
        answer = 1
    else:
        answer = 0
    return answer