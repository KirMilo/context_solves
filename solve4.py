from collections import defaultdict


def binary_search(array: list, value: int, high: int) -> int:
    if value > array[high]:
        return high

    low = 0
    mid = high // 2
    while array[mid] != value and low <= high:
        if value > array[mid]:
            if array[low + 1] > value:
                mid = low
                break
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return mid


def get_left_right(a: list, high: int) -> tuple[int, int]:
    left_ = right_ = 0
    if start <= a[-1]:
        right_ = binary_search(a, stop, high)
        left_ = binary_search(a, start, right_)
        if start == a[left_]:
            left_ -= 1
    return a[left_], a[right_]


orders1 = defaultdict(int)
orders2 = defaultdict(int)
orders1[0] = 0
orders2[0] = 0

# отсортированные по возрастанию суммы заказов от 1-го до n-го
orders1_asc = dict()
orders2_asc = dict()

n = int(input())

for _ in range(n):
    start, stop, cost = map(int, input().split())
    orders1[start] += cost
    orders2[stop] += stop - start

# Заполнение сумм по возрастанию
sorted_orders1 = sorted(orders1)
tmp = 0
for start in sorted_orders1:
    tmp += orders1[start]
    orders1_asc[start] = tmp

sorted_orders2 = sorted(orders2)
tmp = 0
for end in sorted_orders2:
    tmp += orders2[end]
    orders2_asc[end] = tmp


high1 = len(sorted_orders1) - 1
high2 = len(sorted_orders2) - 1
output = []


q = int(input())

for out in range(q):
    start, stop, request = map(int, input().split())

    if request == 1:
        left, right = get_left_right(sorted_orders1, high1)
        if left == right and start == orders1[left]:
            result = orders1[left]
        else:
            result = orders1_asc[right] - orders1_asc[left]
    else:
        left, right = get_left_right(sorted_orders2, high2)
        if left == right and start == orders2[left]:
            result = orders2[left]
        else:
            result = orders2_asc[right] - orders2_asc[left]
    output.append(result)

print(*output)
