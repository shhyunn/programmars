def solution(phone_book):
    #한 번호가 다른 번호의 접두어인 경우가 있는지 확인
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 False 반환
    pb = len(phone_book)
    phone_book.sort()
    for i in range(pb-1):
       if phone_book[i+1].startswith(phone_book[i]):
            return False
                

            # n1, n2 = 0, 0

            # while True:
            #     if n1 >= len(ph1) or n2 >= len(ph2):
            #         return False
                
            #     if ph1[n1] == ph2[n2]:
            #         n1 += 1
            #         n2 += 1
            #         continue
            #     else:
            #         break   

    return True

print(solution(["123","456","789"]))