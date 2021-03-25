'''
단어공부
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
1. 문자를 입력
2. 횟수체크 , 동일한게 2개이상이면 ?
3. 아니면 그 문자를 대문자로 출력
'''

s = input()

m = {string:0 for string in s}
for j in range(len(s)):
    if s[j] in m:
        m[s[j]] += 1
    else:
        m[s[j]] = 1
# print(max(m.values()))
# count = 0
# print(max(m))
# for j in m.values():
#     if max(m.values()) == j:
#         count += 1
#         print(m.values(j))
# print(count)
# if count > 1:
#     print("?")
# else:
#     t = max(m.keys())
#     print(t.upper())
# # if max(m.values()):
# #     print("?")
# # else:
# #     t = max(m.keys())
# #     print(t.upper())