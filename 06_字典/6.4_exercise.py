# 创建多个以宠物名称命名的字典，每个字典中包含宠物类型及主人姓名，再将字典存储在一个名为pets的列表中
panghu = {'pet_type': 'cat', 'owner_name': 'tracy'}
doudou = {'pet_type': 'dog', 'owner_name': 'linda'}
maomao = {'pet_type': 'dog', 'owner_name': 'joice'}
huihui = {'pet_type': 'cat', 'owner_name': 'ken'}

pets = [panghu, doudou, maomao, huihui]

loc = locals()
print(loc)
def namestr(variable):
    for key in loc:
        if loc[key] == variable:
            return key


for pet in pets:
    print(namestr(pet).title() + " is " + pet['owner_name'].title() + "'s " + pet['pet_type'] + ".")



# 创建字典存储三个人的名字及喜欢的地方
favorite_places = {'tracy': ['french', 'italy', 'germany'],
                   'tom': ['china', 'japan', 'indian'],
                   'joice': ['america']}
for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + name.title() + "'s favorite country is: ")
        for country in places:
            print("\t" + country.title())
    else:
        print("\n" + name.title() + "'s favorite countries are: ")
        for country in places:
            print("\t" + country.title())


# 创建cities字典，将三个城市名用作键，对于每座城市都创建一个字典，其中包含城市所属国家、人口约数和有关该城市的事实
# 将每座城市的名字和它的信息打印出来
cities = {"shanghai": {"country": "china", "population": 1500000, "fact": "Shanghai is the financial center of China."},
          "los angeles": {"country": "america", "population": 2000000, "fact": "Los angeles is the second biggist city of America."},
          "Tokyo": {"country": "japan", "population": 1000000, "fact": "Tokyo is the capital city of Japan."}}
for city, city_info in cities.items():
    print("\n" + city.title())
    print("This city is in " + city_info["country"].title() + ".")
    print("Its population is " + str(city_info["population"]) + ".")
    print(city_info["fact"])