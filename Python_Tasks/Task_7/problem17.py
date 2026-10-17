# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separate_numbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = s[:length]
        if first.startswith("0"):
            continue

        expected = ""
        number = int(first)
        while len(expected) < len(s):
            expected += str(number)
            number += 1

        if expected == s:
            return f"YES {first}"

    return "NO"

q = int(input())
for _ in range(q):
    print(separate_numbers(input().strip()))
