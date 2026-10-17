# Problem 11: Two Strings
# HackerRank: https://www.hackerrank.com/challenges/two-strings/problem

def two_strings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

p = int(input())
for _ in range(p):
    s1 = input().strip()
    s2 = input().strip()
    print(two_strings(s1, s2))
