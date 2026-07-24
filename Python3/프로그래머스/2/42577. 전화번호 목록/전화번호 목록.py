'''
각 전화번호의 길이는 1이상 20 이하
dict1 : 접두사가 들어있는 딕셔너리
list1 : 입력 배열 sort


'''

def solution(phone_book):
    answer = True
    list1 = sorted(phone_book)
    dict1 = {}
    
    # print(list1)
    for i in list1:
        text=""
        for z in i:
            text += z
            
            if text in dict1:
                return False
            else:
                if text == i:
                    dict1[text] = 0
    return True
            