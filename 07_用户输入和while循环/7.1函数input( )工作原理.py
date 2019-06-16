# 获取用户输入的文本
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 获取用户输入的姓名
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")


# 提示超过一行时
prompt = "If you tell us who yo are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")


# 使用int()获取数值输入
age = input("How old are you? ")
print(age)
print(type(age))


# 判断身高是否满足要求
height = int(input("How tall are you, in inches? "))

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


# 利用求模运算符判断一个数是奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " +str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")