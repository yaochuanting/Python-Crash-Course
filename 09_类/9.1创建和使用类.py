# 创建dog类
class Dog:
    """一次模拟小狗的简单测试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下时"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令打滚时"""
        print(self.name.title() + " rolled over!")



# 创建一个表示特定小狗的实例
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")


# 调用方法
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()


# 创建多个实例
my_dog = Dog('Willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()