'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기
ex) 1924에서 수 두개 제거
[19, 12, 14,92,94,24]
이 중 가장 큰 숫자는 94
# 뒤숫자보다 작은걸 제외시키면될듯
'''

def solution(number, k):
    answer = ''
    new_arr = list(number)
    stack = []
    count = k
    stack.append(int(new_arr[0]))
    for i in range(1,len(new_arr)):
        new_arr[i] = int(new_arr[i])
        if new_arr[i] >= stack[0] and count > 0:
            del stack[0]
            stack.append(new_arr[i])
        else:
            stack.append(new_arr[i])
        count -= 1
        print(stack)

    return answer

number = "4177252841"
k = 4
print(solution(number,k))