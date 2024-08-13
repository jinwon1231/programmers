def solution(price, money, count):
    answer = 0
    for i in range(1, count + 1):
        answer = answer + int(i) * int(price)
    if money <= answer:
        answer = answer - money
    else:
        answer = 0

    return answer