'''
알파벳 찾기

알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

## 알파벳리스트체크
string 패키지내에
ascii_lowercase 소문자

## 이 문자는 아스키코드범위를 이용해서 리스트를 만들고
find함수를 통해 인덱스 반환하면 된다. 무자열안에 내가 찾는 문자위치 반환!
다만 없다면 -1


'''
# from sys import stdin
# import string
#
# s = stdin.readline().strip()
# s = list(s)
# for i in range(len(string.ascii_lowercase)):
#     if string.ascii_lowercase[i] in s:
#         for j in range(len(s)):
#             if string.ascii_lowercase[i] == s[j]:
#                 print(j,end=' ')
#     else:
#         print(-1,end=' ')

from sys import stdin
s = stdin.readline()
a_list = list(range(97,123)) # 아스키코드 숫자범위
for x in a_list:
    print(s.find(chr(x)))