def solution(s):
    answer = ''
    list = []
    for i in range(len(s)):
        list.append(int(ord(s[i])))

    list.sort(reverse=True)

    for j in range(len(list)):
        answer += chr(list[j])

    return answer


# 더 좋은방법
def solution2(s):
    s = list(s)
    return ''.join(sorted(s,reverse=True))

print(solution('Zbcdefg'))