# 8-6
def city_country(city, country):
    info_str = city + ", " + country
    return info_str.title()

info_str1 = city_country('Shanghai', 'China')
print(info_str1)


# 8-7
def make_album(singer, album_name, num=''):
    album_dir = {}
    album_dir['singer'] = singer
    album_dir['album_name'] = album_name

    if num:
        album_dir['num'] = num

    return album_dir

album1 = make_album('Jolin Cai', 'Beautiful Life', '15')
print(album1)


# 8-8
def make_album(singer, album_name):
    album_dir = {'singer': singer, 'ablum_name': album_name}

    return album_dir

while True:
    print("\nPlease tell me some information of your favorite album: ")
    print("You can input 'q' at any time if you want.\n")

    singer_name = input("Please tell me the name of the singer: ")
    if singer_name == 'q':
        break

    album_name = input("Please tell me the name of the album: ")
    if album_name == 'q':
        break

    album_info = make_album(singer_name, album_name)
    print(album_info)