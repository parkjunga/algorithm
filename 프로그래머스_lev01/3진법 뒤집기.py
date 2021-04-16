'''
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    answer = 0
    tmp = ""
    while n: # 0 은 거짓이니까
        remain = n % 3 #  나머지
        n = n //3  # 나누기
        tmp = str(remain) + tmp
    tmp = tmp[::-1] # 문자 뒤집기
    answer = int(tmp,3)
    return answer

n = 125
ans = solution(n)
print(ans)