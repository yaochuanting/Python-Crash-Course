# 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])

# 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-2:])

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players in my team: ")
for player in players[0:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)