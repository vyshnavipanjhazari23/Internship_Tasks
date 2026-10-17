# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weights = set()
previous = ""
run_length = 0

for ch in s:
    if ch == previous:
        run_length += 1
    else:
        previous = ch
        run_length = 1
    weights.add((ord(ch) - ord("a") + 1) * run_length)

for query in queries:
    print("Yes" if query in weights else "No")
