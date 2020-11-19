'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
끝나는 부분 명시위해서
'''

from sys import stdin
try:
    while True:
        A, B = map(int, stdin.readline().split())
        print(A + B)
except:
    exit()