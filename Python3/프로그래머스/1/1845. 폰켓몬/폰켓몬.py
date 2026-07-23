'''
겹치지 않는 포켓몬
N/2마리 선택 방법


'''
def solution(nums):
    answer = 0
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    
    dict_len = len(dict)
    if dict_len <= len(nums)/2:
        answer = dict_len
    else:
        answer = len(nums)/2
    
    return answer