# 使用json.dump()和 json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'D:\\Python_work\\10_文件和异常\\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)






# 使用json.load()将这个列表读取到内存
import json
filename = 'D:\\Python_work\\10_文件和异常\\numbers.json'

with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)








# 保存和读取用户生成的数据
import json

username = input("What is your name?")

filename = "D:\\Python_work\\10_文件和异常\\username.json"

with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("W'll remember you when you come back, " + username.title() + "!")








# 再编写一个程序，向其名字被存储的用户发出问候
import json

filename = "D:\\Python_work\\10_文件和异常\\username.json"

with open(filename, 'r') as file_object:
    username = json.load(file_object)
    print("Welcome back, " + username.title() + "!")







# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
import json

filename = "username1.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember when you come back, " + username.title() + "!")
else:
    print("Welcome back, " + username.title() + "!")










import json
def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username2.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username.title() + "!")

greet_user()






# 重构
import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username3.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username.title() + "!")
    else:
        username = input("What is your name? ")
        filename = "username3.json"
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username.title() + "!")


greet_user()
