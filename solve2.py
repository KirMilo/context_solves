from collections import defaultdict


def get_total_time_for_id(order_id: str) -> int:
    total_time = 0
    for start, finish in zip(sorted(orders[order_id][0]), sorted(orders[order_id][1])):
        total_time += ((finish[0] - start[0]) * 24 + finish[1] - start[1]) * 60 + finish[2] - start[2]
    return total_time


orders = defaultdict(list[list[list[int]]])

n = int(input())

for _ in range(n):
    order = input().split()
    if not orders.get(order[-2]):
        orders[order[-2]] = [[], []]

    if order[-1] == "A":
        orders[order[-2]][0].append([int(elem) for elem in order[:3]])
    elif order[-1] != "B":
        orders[order[-2]][1].append([int(elem) for elem in order[:3]])

result = []

for order in map(str, sorted(map(int, orders))):
    result.append(get_total_time_for_id(order))

print(*result)

