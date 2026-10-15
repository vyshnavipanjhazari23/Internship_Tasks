string = input()
position, character = input().split()

position = int(position)

result = string[:position] + character + string[position + 1:]
print(result)