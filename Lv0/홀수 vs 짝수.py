def solution(num_list):
    answer = 0
    a = 0
    b = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            a = a + num_list[i]
        else:
            b = b + num_list[i]
    if a >= b:
        answer = a
    else:
        answer = b

    return answer