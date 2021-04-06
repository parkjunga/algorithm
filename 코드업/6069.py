'''
6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기

평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
'''

what = input()
if what == 'A':
    print('best!!!')
elif what == 'B':
    print('good!!')
elif what == 'C':
    print('run!')
elif what == 'D':
    print('slowly~')
else:
    print('what?')