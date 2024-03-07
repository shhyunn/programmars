def solution(nums):
    answer = 0
    #최대한 다양한 종류의 포켓몬을 가지고자 함
    #n/2마리 선택 가능
    set_nums = set(nums)
    ll = len(nums)
    if ll//2 <= len(set_nums):
        answer = ll//2
    else:
        answer = len(set_nums)
        
    return answer