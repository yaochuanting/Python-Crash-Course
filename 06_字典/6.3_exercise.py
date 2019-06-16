# 打印河流和国家，单独打印河流名称，单独打印国家名称
rivers_positions = {'nile': 'egypt', 'Huanghe': 'china', 'danube': 'germany'}
for river, country in rivers_positions.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print("\n")
for river in rivers_positions.keys():
    print(river.title())
print("\n")
for country in rivers_positions.values():
    print(country.title())



# 创建应可接受调查的人员名单，部分在字典中，部分不在字典中，参与调查表示感谢，未参与调查邀请调查
members = ['jen', 'alice', 'tom', 'ken', 'sarah', 'allen', 'edward', 'phil']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for member in members:
    if member in favorite_languages.keys():
        print(member.title() + ", thank you for your participation!")
    else:
        print(member.title() + ", would you like to join our poll?")

