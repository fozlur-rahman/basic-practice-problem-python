n = int(input())
a = list(map(int, input().split()))

min_num = min(a)
max_num = max(a)
min_index = a.index(min_num)
max_index = a.index(max_num)

a[min_index],a[max_index]=a[max_index],a[min_index]

print(*a)