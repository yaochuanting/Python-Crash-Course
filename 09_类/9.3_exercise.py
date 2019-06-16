# 9-6
# 编写父类
class Restaurant():
    """创建一个餐厅的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The cuisine type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        print("The restaurant is open.")

    def describe_num_served(self):
        print("The restaurant has served " + str(self.number_served) + ' people.')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increment):
        self.number_served += increment



# 编写冰淇淋小店的子类
class IceCreamStand(Restaurant):
    """冰淇淋小店的特殊之处"""
    def __init__(self, restaurant_name, cuisine_type):
        """
        初始化父类的属性
        在初始化子类的属性
        """

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'sweet', 'lemon']

    def describe_icecream(self):
        for flavor in self.flavors:
            print(flavor)


my_icecreamstand = IceCreamStand('Teddy', 'dessert')
print(my_icecreamstand.describe_icecream())





# 9-6
# 子类的方法 _init()_
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make.title() + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# 将电瓶的属性和方法提取出来，放到battery类中
#并将Battery实例用作ElectricCar类的一个属性
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def update_battery(self):
        self.battery_size = 85


    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += ' miles on a full change.'
        print(message)



# 定义子类
class ElectricCar(Car):
    """电动汽车的特殊之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
