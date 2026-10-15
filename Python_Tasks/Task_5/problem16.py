# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_sizes = Counter(map(int, input().split()))
customers = int(input())

total_earnings = 0

for _ in range(customers):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        total_earnings += price
        shoe_sizes[size] -= 1

print(total_earnings)
