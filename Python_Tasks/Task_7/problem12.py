# Problem 12: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

a = input().strip()
b = input().strip()

count_a = Counter(a)
count_b = Counter(b)

deletions = sum((count_a - count_b).values()) + sum((count_b - count_a).values())
print(deletions)
