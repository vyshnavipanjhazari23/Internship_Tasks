# Problem: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

string = input()
index, character = input().split()
index = int(index)

result = string[:index] + character + string[index + 1:]
print(result)
