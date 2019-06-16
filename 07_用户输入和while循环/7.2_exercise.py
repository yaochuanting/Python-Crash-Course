# 提示用户输入配料，在用户输入quit时结束循环，每输入一次配料打印一条消息
prompt = "Please enter the tooping of pizza: "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print("We will add " + toppings.lower() + " in the pizza.")



# 询问用户年龄，输出票价
promt = "Please tell me your age: "

while True:
    age = input(promt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("The ticket price is free.")
    elif int(age) <= 12:
        print("The ticket price is $10.")
    else:
        print("The ticket price is $15.")
