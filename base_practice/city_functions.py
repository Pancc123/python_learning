def city_country(city,country,population=''):
	if population:
		cy_home=city.title()+','+country.title()+' -population '+population
	else:
		cy_home=city.title()+','+country.title()
	return cy_home
