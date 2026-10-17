# Problem 4: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

def funny_string(s):
    values = [ord(ch) for ch in s]
    reverse_values = [ord(ch) for ch in s[::-1]]

    for i in range(1, len(s)):
        if abs(values[i] - values[i - 1]) != abs(reverse_values[i] - reverse_values[i - 1]):
            return "Not Funny"
    return "Funny"

t = int(input())
for _ in range(t):
    print(funny_string(input().strip()))
