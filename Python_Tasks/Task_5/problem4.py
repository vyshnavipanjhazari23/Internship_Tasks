# Problem: Find a String
# HackerRank: https://www.hackerrank.com/challenges/find-a-string/problem

string = input().strip()
substring = input().strip()

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        count += 1

print(count)
