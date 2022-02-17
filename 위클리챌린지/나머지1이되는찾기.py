def solution(n):
    answer = 0
    tmp = n-1
    tmp_num = 0
    for i in range(1,tmp+1):
        if tmp%i == 0:
            print(i)
            if tmp_num < i and i % i+1 == 0:
                tmp_num = i
    print(tmp_num)
    return answer

n = 10
ans = solution(n)
print(ans)