# 使用while循环数数
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1



# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)



# 使用标志
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



# 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")



# 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


