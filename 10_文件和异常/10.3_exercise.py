# 10-6 加法运算：编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的 任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
# 编写的代码放在一个 while 循环中，让 用户犯错（输入的是文本而不是数字）后能够继续输入数字。

print("Give me tow numbers, and I will add them.")
print("Enter 'q' if you want to quit.")

while True:

        first_number = input("\nThe first number is: ")
        if first_number == 'q':
            break
        second_number = input("\nThe second number is: ")
        if second_number == 'q':
            break

        try:
            answer = int(first_number) + int(second_number)
        except ValueError:
            print("You must enter two numbers.")
        else:
            print(first_number + " add " + second_number + " equals " + str(answer) + ".")




# 创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息
from read_name import dog_cat_name

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    dog_cat_name(filename)





