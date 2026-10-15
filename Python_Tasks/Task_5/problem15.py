# Problem: Lists
# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == "__main__":
    n = int(input())
    items = []

    for _ in range(n):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            items.insert(int(command[1]), int(command[2]))
        elif operation == "print":
            print(items)
        elif operation == "remove":
            items.remove(int(command[1]))
        elif operation == "append":
            items.append(int(command[1]))
        elif operation == "sort":
            items.sort()
        elif operation == "pop":
            items.pop()
        elif operation == "reverse":
            items.reverse()
