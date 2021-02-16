'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기
'''

N = int(input())
#1 1부터 N까지 이면 N+1
for i in range(1,N+1):
    # if i%2 != 0:
    #     print("1) 홀수",i)
    if i%2 ==1:
        print("1) 홀수",i)

#2
sum = 0
for i in range(1,N+1):
    sum += i
print("2) 합계",sum)

# 3 N까지 약수구하기
for i in range(1,N+1):
    if N%i == 0:
        print("3)",i, end= ' ') # 줄바꾸지않고 출력

