# Problem: Capitalize!
# HackerRank: https://www.hackerrank.com/challenges/capitalize/problem

import string

def solve(s):
    return string.capwords(s, " ")

if __name__ == "__main__":
    s = input()
    print(solve(s))
