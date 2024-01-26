#!/usr/bin/env python3

# inputs for country, visits and list of cities
country = input()
visits = int(input())
list_of_cities = eval(input())

# storing list of with dictionaries
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# add new country function
def add_new_country(name, times_visited, cities_visited):
    # empty new country dictionary
    new_country = {}
    # add keys to the new country empty dictionary
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    # copy our new dictionary to our dictionary list
    travel_log.append(new_country.copy())

# call our function
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")

