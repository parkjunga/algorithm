'''
아스키코드
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 아스키코드를 구할때 그냥 문자열일경우 strip을 사용하지 않으면 \n이 들어가기때문에 1이아닌 2로 길이값이 잡힌다.
따라서 문자가 되지않아 변환되지 않고

TypeError: ord() expected a character, but string of length 2 found
발생한다.
'''

from sys import stdin

m = stdin.readline().strip()
print(ord(m))
