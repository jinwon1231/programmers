def solution(intStrs, k, s, l):
    answer = []
    for Str in intStrs:
        if int(Str[s:s+l])>int(k):
            answer.append(int(Str[s:s+l]))
    return answer