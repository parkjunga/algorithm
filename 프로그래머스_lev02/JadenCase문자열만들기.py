'''
string.upper()
string.capitalize()
string.title()
'''
def solution(s):
    answer = ''
    s = s.lower()
    s2 = s.split(' ')
    for i in range(len(s2)):
        s2[i] = s2[i].capitalize()
    answer = ' '.join(s2)
    return answer

s = "3people unFollowed me"
print(solution(s))