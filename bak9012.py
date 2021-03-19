# 괄호문제 스택이용?

import collections
def test(s):
    stack = []
    ans = 'No'
    deq = collections.deque(s)
    for i in range(len(deq)):
        if deq[i] == '(':
            stack.append(deq[i])
        else:
            if len(stack) > 0:
                stack.pop()
        deq.popleft()
    return ans
n = int(input())
for i in range(n):
    s = input()
    ans = test(s)
    print(ans)
