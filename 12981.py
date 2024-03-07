def solution(n, words):
    answer = [0,0]
    #이전에 등장했던 단어 사용 불가, 한글자인 단어 사용 불가
    #가장 먼저 탈락하는 사람의 번호 및 자신의 몇번쨰 차례에 탈락하는지
    cnt = 1
    used = []
    num = 0
    prev = words[0][0]
    for word in words:
        num += 1
        if word in used or prev != word[0]:
            answer = [num,cnt]
            break

        used.append(word)
        prev = word[-1]
        if num == n:
            num = 0
            cnt += 1

    return answer