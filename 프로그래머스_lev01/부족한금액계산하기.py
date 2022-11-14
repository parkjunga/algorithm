def solution(price, money, count):
    answer = 0
    result_price = 0

    for i in range(1,count+1):
        result_price += i * price

    if money < result_price:
        answer = result_price - money

    return answer


answer = solution(3,20,4)
print(answer)