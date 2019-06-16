# 处理ZeroDivisionError 异常
print(5/0)



# 使用try-except 代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero!")



# 使用异常避免崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to to quit." )

while True:
    first_number = input("The first number is: ")
    if first_number == 'q':
        break
    second_number = input("The second number is: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)




# 处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist.")




# 分析文本
filename = 'D:\\Python_work\\10_文件和异常\\alice.txt'

try:
    with open(filename, 'r') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


