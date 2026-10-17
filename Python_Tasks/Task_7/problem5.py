# Problem 5: Alternating Characters
# HackerRank: https://www.hackerrank.com/challenges/alternating-characters/problem

def alternating_characters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

q = int(input())
for _ in range(q):
    print(alternating_characters(input().strip()))
