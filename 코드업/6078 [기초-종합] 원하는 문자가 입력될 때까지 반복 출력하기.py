'''
6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기

영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.

'''
n = input()
while n != 'q':
    print(n)
    n = input()
    if n == 'q':
        break
print(n)