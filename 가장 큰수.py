def solution(numbers):
    answer = ''
    a =list(map(str,numbers)) # 문자열로 변환
    # numbers 원소가 1000을 넘지않으므로 3번째까지만 비교
    #sorted(a,key=lambda x: x*3,reverse=True) # 람다함수로 문자열로 변환한 숫자중 가장 큰 숫자를 거꾸로 비교 3개씩 비교
    answer = ''.join(sorted(a,key=lambda x: x*3,reverse=True))
    return str(int(answer)) # 0000이라는 특이케이스르 해결하기위해 0000 -> 0


numbers = [0,0,0,0]#[3, 30, 34, 5, 9]
ans = solution(numbers)
print(ans)


'''
플이
1. 먼저 숫자들을 문자열 리스트로 변환시킨다. 
ex) [3, 30, 34, 5, 9 ]-> ["3", "30", "34", "5", "9" ]

2. 문자열을 3개씩 붙여서 내림차순으로 비교한다
즉) 333, 303030 -> 303, 343434 -> 343 , 555, 999 -> 이 숫자들 정렬 

3. 마지막으로 정렬된 숫자를 문자열로 더한다.

4. 특이케이스인 0 0 0 0 을 비교했을때 답이 0000 임으로 0 을 반환하기 위해 0인경우 int로 변환한다음에 다시 str로 반환한다.

'''