def solution(friends, gifts):
    present_arr = [[0 for j in range(len(friends))]for i in range(len(friends))]
    num = 0
    present_num = {}
    present_result = [0 for i in range(len(friends))]
    
    for i in friends:
        present_num[i] = 0
    
    
    # 선물지수 계산
    for i in gifts:
        sep_gifts = i.split()
        a = sep_gifts[0]
        b = sep_gifts[1]
        present_num[a] += 1
        present_num[b] -= 1

        present_arr[friends.index(a)][friends.index(b)] += 1
    
    present_num_value = list(present_num.values())
    
    for i in range(len(friends)):
        for j in range(i+1):
            if present_arr[i][j] > present_arr[j][i]:
                present_result[i] += 1
            elif present_arr[i][j] == present_arr[j][i]:
                if present_num_value[i] > present_num_value[j]:
                    present_result[i] += 1
                elif present_num_value[i] < present_num_value[j]:
                    present_result[j] += 1
            elif present_arr[i][j] < present_arr[j][i]:
                present_result[j] += 1
            else:
                pass
    
    return max(present_result)