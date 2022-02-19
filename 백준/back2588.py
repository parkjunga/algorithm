'''
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
'''

b = int(input())
a = input()

print(int(a[2])*b)
print(int(a[1])*b)
print(int(a[0])*b)
print(int(a)*b)