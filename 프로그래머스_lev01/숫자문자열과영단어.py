def solution(s):
    answer = 0
    new_arr = []
    test = ''
    #s_arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    s_arr = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    for k,v in s_arr.items():
        if k in s :
            s = s.replace(k,v)
    answer = int(s)

    # for i in range(len(s_arr)):
    #     if s_arr[i] in s :
    #         s = s.replace(s_arr[i],'')
    #         new_arr.append(str(i))
    #     elif str(i) in s:
    #         new_arr.append(str(i))
    # answer = ''.join(new_arr)
    # answer = int(answer)
    return answer

s = "one4seveneight"
solution(s)