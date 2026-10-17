# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
odd_counts = sum(1 for count in Counter(s).values() if count % 2)

print("YES" if odd_counts <= 1 else "NO")
