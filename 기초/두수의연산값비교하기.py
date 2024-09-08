def solution(a, b):
    answer = 0
    t1 = str(a) + str(b)
    t2 = 2 * a * b
    if int(t1) > t2:
        answer = int(t1)
    else:
        answer = t2
    return answer


a = 91
b = 2
answer= solution(a,b)
print(answer)