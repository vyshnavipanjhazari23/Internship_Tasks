# Problem: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowels = set("AEIOU")
    length = len(string)

    for i, char in enumerate(string):
        points = length - i
        if char in vowels:
            kevin_score += points
        else:
            stuart_score += points

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
