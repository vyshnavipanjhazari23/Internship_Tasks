# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()
if not s:
    print(0)
else:
    print(1 + sum(1 for ch in s if ch.isupper()))
