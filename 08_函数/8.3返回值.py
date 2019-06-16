# 接受姓和名，返回整洁的姓名
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 增加中间名
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# 让中间名变成可选,python将非空字符串解读为True
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



# 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# 定义一个可选形参：年龄
def build_person(first_name, last_name, age=''):
    """返回一个字典，包含个人信息"""
    if age:
        person = first_name + " " + last_name + " is " + age + "."
    else:
        person = first_name + " " + last_name
    return person.title()

output1 = build_person('jimi', 'hendrix', '17')
print(output1)
output2 = build_person('john', 'lee')
print(output2)


# 增加年龄
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age='27')
print(musician)


# 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name ")
    print("Enter 'q' at any time to quit.")

    f_name = input("First name: ")
    if f_name == 'q':
            break

    l_name = input("Last name: ")
    if l_name == 'q':
            break

    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello, " + formatted_name + "!")



