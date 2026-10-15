m = int(input())
set_a = set(map(int, input().split()))

n = int(input())
set_b = set(map(int, input().split()))

result = sorted(set_a.symmetric_difference(set_b))

for number in result:
    print(number)