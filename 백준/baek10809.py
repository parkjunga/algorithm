'''
문자열
알파벳 찾기

알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

1. 알파벳 소문자를 배열로 받을 수 있는 패키지를 import
2. input으로 받은 값에 위치를 넣을 수 있게 dict 로 변환 기본값은 -1
> 처음 문제에서 포함되지 않는 값은 -1이라고 전재했기 때문에
3. 그다음, 중복되는 값은 위치값을 바꾸지 않고 처음값으로 유지하게끔하기 위해 조건문 추가
4. 담긴 dict를 value만 가져와서 문자열로 치환

'''
from string import ascii_lowercase

n = input()

t = list(ascii_lowercase)
dic_t = dict.fromkeys(t,-1)

for i in range(len(n)):
    if dic_t[n[i]] != -1 :
        continue
    else:
        dic_t[n[i]] = i

n = []
for j in dic_t.values():
    n.append(str(j))

result = ' '.join(n)
print(result)