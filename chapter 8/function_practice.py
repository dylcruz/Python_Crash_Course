# 8-1
def write_message():
	print("we're learning about functions")

# 8-2
def favorite_book(title):
	print("One of my favorite books is " + title.title() + ".")

write_message()
favorite_book('Harry Potter')

# 8-3 & 8-4
def make_shirt(size='Large', message='I love Python.'):
	print('\nShirt Size: ' + size)
	print('Printed Message: ' + message)

make_shirt()
make_shirt('Small', 'Class of 2018')
make_shirt(message='Class of 2019', size='Medium')


print()

# 8-5
def describe_city(city, country='USA'):
	print(city + ' is in ' + country)
describe_city('Berlin', 'Germany')
describe_city('Paris', 'France')
describe_city('New York')

print()

# 8-6
def city_country(city, country):
	print('"' + city.title() + ", " + country.title() + '"')
city_country('paris', 'france')
city_country('berlin', 'germany')
city_country('new york', 'usa')

print()

# 8-7
def make_album(artist, title, tracks=""):
	if tracks:
		album = {'Artist':artist, 'Title':title, 'Tracks':tracks}
	else:
		album = {'Artist':artist, 'Title':title}
	return album

album1 = make_album("Kanye West", "Graduation")
album2 = make_album("Nas", "Illmatic")
album3 = make_album("Flatbush Zombies", "D.R.U.G.S", 18)

print(album1)
print(album2)
print(album3)

print()

# 8-8
while True:
	print("- Please enter the album information -")
	print("(enter 'q' at any time to quit")
	artist = input("Artist: ")
	if artist == 'q':
		break
	title = input("Title: ")
	if title == 'q':
		break
	album = make_album(artist, title)
	print(album)