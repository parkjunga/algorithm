def solution(s):
    answer = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    print(s[2:4])
    for i in range(len(s)):
        #print(i)
        if s[i:i*2]:
            ss = ''
            ss = s[i:i*2]
            print(ss)

    return answer

'''
baabaa	1
cdcd	0
'''

solution('baabaa')