import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefix_sum = []
total = 0

for rooms in a:
    total += rooms
    prefix_sum.append(total)


for room in b:
    dorm_index = bisect.bisect_left(prefix_sum, room)
    previous_rooms = prefix_sum[dorm_index - 1] if dorm_index > 0 else 0
    local_room = room - previous_rooms
    print(dorm_index + 1, local_room)