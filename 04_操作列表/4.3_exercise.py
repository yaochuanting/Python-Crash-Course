# 打印列表前三个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are: ")
for player in players[:3]:
    print(player.title())

# 打印列表中间三个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are: ")
for player in players[1:4]:
    print(player.title())
