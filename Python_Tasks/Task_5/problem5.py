# Problem: String Validators
# HackerRank: https://www.hackerrank.com/challenges/string-validators/problem

text = input()

print(any(char.isalnum() for char in text))
print(any(char.isalpha() for char in text))
print(any(char.isdigit() for char in text))
print(any(char.islower() for char in text))
print(any(char.isupper() for char in text))
