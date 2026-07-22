def solution(participant, completion):
    h1 = dict.fromkeys(participant, 0)
    answer = ''
    
    for i in participant:
        h1[i] += 1
    
    for i in completion:
        h1[i] -=1
        
    for i in h1:
        if h1[i] > 0:
            answer = i
            h1[i]-=1

    return answer