'''
문자열과 내장함수
'''

msg = "It is Time" # 이걸 대문자로 변경
print(msg.upper())
print(msg.lower()) # 소문자
print(msg)

tmp = msg.upper() # 대문자화된 변수
print(tmp)
print(tmp.find('T')) # T라는 문자를 찾아라 , 더불어 이렇게 찾아서 인덱스번호를 반환한다.
print(tmp.count('T')) # 문자열에서 T가 몇개인지 말해라
print(msg[:2]) # msg라는 문자에서 앞에 두개까지만 뽑기 인덱스 2번전까지 뽑기
for i in range(len(msg)):
    print(msg[i], end=' ')

print()
''' 
isalpha() 공백을 제외하고 출력됨
'''
for x in msg:
    if x.isalpha(): # 대문자인 것만
      print(x, end= ' ')
print()

tmp2 = 'AZ'
for x in tmp2:
    print(ord(x)) # 아스키넘버출력


tmp2 = 'az'
for x in tmp2:
    print(ord(x)) # 아스키넘버출력

tmp2 = 65
print(chr(tmp2)) # 아스키넘버에 대응되는 문자를 출력 