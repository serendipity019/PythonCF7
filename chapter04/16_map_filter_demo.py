cities = ["london", "Paris", "Athens", "barcelona", "Casablanka"]

# step 1. filter city names longer than 5 characters (usin filter and lambda)
long_cities = filter(lambda city: len(city) > 5, cities)
#print(*long_cities)

# step 2. Capitalize the first letter
cap_length_cities = list(map(lambda city: city.title(), long_cities))
print(cap_length_cities)


# second way All in one...
clc = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

# list compr
cap_length_cities_compr = [city.title() for city in cities if len(city) > 5]
print(cap_length_cities_compr)