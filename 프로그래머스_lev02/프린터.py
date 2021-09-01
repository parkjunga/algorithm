def solution(priorities, location):
    answer = 0
    new = list(enumerate(priorities))
    # 거꾸로 + 순서
    new.sort(key=lambda x:(x[1],x[0]),reverse=True)
    print(new)
priorities = [1, 1, 9, 1, 1, 1] # 중요도 순서
location = 0# 내가 인쇄 요청한 문서 몇 번쟤

solution(priorities,location)



'''
아주 심플b ? gcd(b,a%b) : a

'''