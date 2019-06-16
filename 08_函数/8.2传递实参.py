# 位置实参
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("cat", "Panghu")



# 调用函数多次
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')



# 关键字实参
def describe_pet(animal_type, pet_name):
    '''显示宠物的姓名'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 默认值
def describe_pet(pet_name, animal_type='dog'):
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')



# 等效的函数调用
def make_skirt(size, info):
    print("The size of the shirt is " + str(size) + ".")
    print("")