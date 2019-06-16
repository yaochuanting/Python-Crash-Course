# 检查是否相等
car = 'bmw'
print(car == 'audi')



# 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")



# 比较数字
age = 18
print(age == 18)



# 检查数字是否不相等
answer = 18
if answer != 43:
    print("That is not the correct answer. Please try again!")



# 检查多个条件
# 使用and检查多个条件
age_0 = 18
age_1 = 25
print(age_0 < 18 and age_1 > 18)

# 使用or检查多个条件
age_0 = 19
age_1 = 27
print(age_0 < 18 or age_1 > 20)



# 检查特定值是否包含在列表中
requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping)



# 检查特定值是否不包含在列表中
banned_users = ['andrew', 'caroline', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")



# 布尔表达式
