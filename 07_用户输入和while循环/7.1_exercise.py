# 询问用户想要一辆什么样的汽车 并打印文本
car_type = input("Please tell you what kind of car do you want: ")
print("Let me see if I can find you a " + car_type.lower().title() + ".")


# 餐厅订餐，如果超过8人指出没有空桌，否则输入有空座
number = int(input("How many people will join the dinner? "))

if number > 8:
    print("There is no suitable table available.")
else:
    print("There is table available.")



# 判断一个数是否是10的倍数
number = int(input("Enter a number: "))

if number % 10 == 0:
    print("Yes.")
else:
    print("No.")
