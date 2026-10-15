# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set(student[1] for student in students))
second_lowest = scores[1]

for name in sorted(student[0] for student in students if student[1] == second_lowest):
    print(name)
