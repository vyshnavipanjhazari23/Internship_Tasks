# Problem 2: The Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
room_numbers = list(map(int, input().split()))

unique_sum = sum(set(room_numbers))
captain_room = (unique_sum * k - sum(room_numbers)) // (k - 1)

print(captain_room)
