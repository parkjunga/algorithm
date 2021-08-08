def solution(price, money, count):
    answer = -1
    sum = 0
    for i in range(1,count+1):
        sum += price * i
        if sum < money:
            answer = 0
        else:
            answer = sum - money
    return answer

price = 3 # 이용료
money = 20 # 현재 내가 가지고있는금액
count = 4 # 타고자하는 횟수

print(solution(price, money, count))