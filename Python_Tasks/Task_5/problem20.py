# Problem: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))
    last = float("inf")
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            chosen = blocks.popleft()
        else:
            chosen = blocks.pop()

        if chosen > last:
            possible = False
            break

        last = chosen

    print("Yes" if possible else "No")
