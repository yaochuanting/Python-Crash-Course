# 遍历所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)



favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")



# 遍历字典中所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
for name in favorite_language.keys():
    print(name.title())



# 遍历字典中的名字，但在名字为指定的朋友名字时，打印一条消息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")



# 按顺序遍历字典中所有的键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")



# 遍历字典中所有的值 set()函数用于保留非重复项
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

