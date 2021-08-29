
def get_formatted_city(city, country, population=''):
	if population:
		formatted_name = city + ', ' + country + ' - population ' + str(population)
	else:
		formatted_name = city + ', ' + country
	return formatted_name.title()

