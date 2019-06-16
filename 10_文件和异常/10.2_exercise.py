# 将用户输入的名字存储到文件 guest.txt中
name = input("Please tell me your name: ")
filename = 'D:\\Python_work\\10_文件和异常\\guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name.title())


# 编写一个 while 循环，提示用户输入其名字。
# 用户输入其名字后， 在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中
prompt = "\nTell me the name: "
prompt += "\nEnter 'quit' to end the program."
name = ''
filename = "D:\\Python_work\\10_文件和异常\\guest_book.txt"
while True:
    name = input(prompt)
    if name != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write("Hello, " + name.title() + '\n')
    elif name == 'quit':
        break



prompt = "\nTell me the name: "
prompt += "\nEnter 'quit' to end the program."
filename = "D:\\Python_work\\10_文件和异常\\guest_book.txt"
name = input(prompt)

with open(filename, 'a') as file_object:
    while name != 'quit':
        file_object.write("Hello, " + name.title() + '!')
        name = input(prompt)






