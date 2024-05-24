def solution(cipher, code):
    answer = ''
    # 임의의숫자삽입
    cipher = 'a'+cipher
    for i in range(len(cipher)):
        if i % code == 0 and i > 0:
            answer += cipher[i]
    return answer

cipher = "dfjardstddetckdaccccdegk"
code = 4
solution(cipher,code)