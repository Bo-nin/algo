import heapq


def solution(N, coffee_times):
    answer = []
    coffee_list = []
    cu_ind = 0
    min_coffee_num = 0
    flag = False
    while cu_ind < len(coffee_times):
        while len(coffee_list) <N:
            heapq.heappush(coffee_list,(min_coffee_num+coffee_times[cu_ind],cu_ind+1))
            cu_ind += 1
            if cu_ind == len(coffee_times):
                break
        if flag:
            break
        min_coffee_num = coffee_list[0][0]
        ej_coffee = []
        while coffee_list:
            if min_coffee_num != coffee_list[0][0]:
                break
            coffee_time, ej_ind = heapq.heappop(coffee_list)
            ej_coffee.append(ej_ind)
        ej_coffee.sort()
        answer.extend(ej_coffee)
    while coffee_list:
        _,ind = heapq.heappop(coffee_list)
        answer.append(ind)
    return answer