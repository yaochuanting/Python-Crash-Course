# 传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



# 条print语句替换为一个循环，对配料列表进行遍历
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')




# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")

    for topping in toppings:
        print("-" + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')




# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切信息"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)