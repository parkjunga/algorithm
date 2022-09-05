'''
그리드 알고리즘

다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다.
다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,

전체를 뒤집으면 1110011이 된다.
4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.

해결방법
** groupby 라이브러리를 사용

1. 문자열을 groupby 시켜 Key 와 value로 구분
2. groupby 된 갯수를 1과 0으로 나눠 세서 계산후
3. 둘중 더 작은값을 반환

'''
from itertools import groupby

s = input()


def long_repeat(data):
    one = 0
    zero = 0
    for key, groupingData in groupby(data):
        if int(key) == 1:
            one += 1
        else:
            zero += 1

    if one > zero:
        return zero
    else:
        return one


print(long_repeat(s))