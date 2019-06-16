# 先判断用户名列表是否可为空，再根据if判断结果输出内容
user_names = ['Lisa', 'Alice', 'Tom', 'Ada', 'admin', 'Julia', 'Tracy']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello, would you like to see  status report?")
        else:
            print("Hello " + user_name + ", thank you for logging in again.")
else:
    print("No users.")



# 检查用户名，确保用户名不重复
curren_users = ['alice', 'tom', 'allen', 'bella', 'caroline', 'Jenny']
new_users = ['allen', 'alice', 'cathy' ,'Bella', 'jerry', 'ivy']
for new_user in new_users:
    if new_user.lower() in curren_users:
        print(new_user.title() + " is already taken. Please input a new user name.")
    else:
        print(new_user.title() + " is available.")


# 输入序数
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        number_situation = str(number) + "st"
    elif number == 2:
        number_situation = str(number) + "nd"
    elif number ==3:
        number_situation = str(number) + "rd"
    else:
        number_situation = str(number) + "th"
    print(number_situation)
