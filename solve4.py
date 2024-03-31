from collections import defaultdict

orders1 = defaultdict(int)
orders2 = defaultdict(int)


def binary_search(a: list, value: int, high: int) -> int:
    low = 0
    if value < a[low]:
        return low
    elif value > a[high]:
        return high

    mid = high // 2
    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
            if a[low] > value:
                mid = low - 1
                break
        else:
            if a[high] < value:
                mid = high - 1
                break
            high = mid - 1
        mid = (low + high) // 2

    return mid


def get_left_right(a: list, start_: int, stop_: int, high: int) -> tuple[int, int]:
    left_ = right_ = 0
    if start_ <= a[-1]:
        right_ = binary_search(a, stop_, high)
        left_ = binary_search(a, start_, right_)
        if start_ == a[left_]:
            left_ -= 1
    return a[left_], a[right_]


orders1[0] = 0
orders2[0] = 0

n = int(input())
# t1 = dt.now()

for _ in range(n):
    start, stop, cost = map(int, input().split())
    orders1[start] += cost
    orders2[stop] += stop - start

# отсортированные по возрастанию суммы заказов от 1-го до n-го
orders1_asc = dict()
orders2_asc = dict()

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

q = int(input())

high1 = len(sorted_orders1) - 1
high2 = len(sorted_orders2) - 1
output = []
for out in range(q):
    start, stop, request = map(int, input().split())
    if request == 1:
        left, right = get_left_right(sorted_orders1, start, stop, high1)
        if left == right and start == orders1[left]:
            result = orders1[left]
        else:
            result = orders1_asc[right] - orders1_asc[left]
    else:
        left, right = get_left_right(sorted_orders2, start, stop, high2)
        if left == right and start == orders2[left]:
            result = orders2[left]
        else:
            result = orders2_asc[right] - orders2_asc[left]

    output.append(result)

print(*output)
