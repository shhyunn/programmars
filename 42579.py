def solution(genres, plays):
    answer = []
    dic={key:0 for key in genres}
    for genre,play in zip(genres, plays):
        dic[genre] += play
        
    genre_sort = list(dict(sorted(dic.items(),key=lambda items:items[1],reverse=True)).keys())
    dic2={key:[] for key in genre_sort}
    
    for i,genre in enumerate(genres):
        dic2[genre].append(i)

    for key in dic2.keys():
        dic2[key] = sorted(dic2[key],key=lambda i:plays[i], reverse=True)

    for gen in genre_sort:
        cnt = 0
        for id in dic2[gen]:
            answer.append(id)
            cnt += 1
            if cnt == 2:
                break

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))