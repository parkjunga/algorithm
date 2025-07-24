def solution(s):
    answer = 0
    tmp = s
    o_count = 0
    itmp = int(tmp)
    while itmp > 1:
        s_count = tmp.count('1')
        o_count += tmp.count('0')
        answer += 1
        tmp = str(bin(s_count))
        if '0b' in tmp:
            tmp = tmp[2:]
            itmp = int(tmp)

    return [answer, o_count]


s ="01110"
print(solution(s))