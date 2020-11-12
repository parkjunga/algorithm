def solution(n):
    answer = 0
    i = 0
    while i < n:
        i += 1
        if n%i == 0:
            print("아이값",i)
            answer += i
    return answer

a = solution(12)
print(a)