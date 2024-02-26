def solution(info, edges):
    from collections import deque
    tree = [[] for _ in range(len(info))]

    for edge in edges:
        tree[edge[0]].append(edge[1])

    q = deque([(0,1,0,set())])
    max_sheep = 0

    while q:
        curr,sheep,wolf,visited = q.popleft()
        max_sheep = max(max_sheep,sheep)
        visited.update(tree[curr])

        for i in visited:
            if info[i] == 1:#늑대일 경우
                if sheep != wolf + 1:
                    q.append((i,sheep,wolf+1,visited-{i}))

            else: #양일 경우
                q.append((i,sheep+1,wolf,visited-{i}))

    return max_sheep