import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:#course 개수별로
        order_combinations = [] #조합 저장 리스트
        for order in orders: #주문 별로 조합 계산
            order_combinations += itertools.combinations(sorted(order), course_size) #order 정렬 후, 가능 조합 저장

        most_ordered = collections.Counter(order_combinations).most_common() #모든 주문에서 조합 빈도가 가장 높은 순서대로 정렬
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ] #가장 높은 빈도수와 동일하면서 빈도수는 2 이상인 조합을 result에 저장

    return [ ''.join(v) for v in sorted(result) ] #다시 result 정렬 후 문자열로 join
