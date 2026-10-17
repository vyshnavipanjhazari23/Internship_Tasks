# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS" * (len(s) // 3)

changes = sum(1 for actual, wanted in zip(s, expected) if actual != wanted)
print(changes)
