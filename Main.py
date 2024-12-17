import requests

def get_planets_with_arid_climate():
    url = "https://swapi.dev/api/planets/"
    arid_planet_films = set()

    while url:
        response = requests.get(url).json()
        for planet in response["results"]:
            if "arid" in planet["climate"]:
                arid_planet_films.update(planet["films"])
        url = response.get("next")

    return len(arid_planet_films)

def count_wookies():
    url = "https://swapi.dev/api/people/"
    wookie_count = 0

    while url:
        response = requests.get(url).json()
        for person in response["results"]:
            if any("wookiee" in species_url.lower() for species_url in person["species"]):
                wookie_count += 1
        url = response.get("next")

    return wookie_count

def smallest_starship_in_first_movie():
    film_url = "https://swapi.dev/api/films/1/"
    response = requests.get(film_url).json()
    starships = response["starships"]

    smallest_ship = None
    smallest_length = float("inf")

    for starship_url in starships:
        starship = requests.get(starship_url).json()
        try:
            length = float(starship["length"].replace(",", ""))
            if length < smallest_length:
                smallest_length = length
                smallest_ship = starship["name"]
        except ValueError:
            continue

    return smallest_ship

if __name__ == "__main__":
    # a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?
    print("Películas con planetas áridos:", get_planets_with_arid_climate())

    # b) ¿Cuántos Wookies aparecen en toda la saga?
    print("Número de Wookies:", count_wookies())

    # c) ¿Cuál es el nombre de la aeronave más pequeña en la primera película?
    print("Aeronave más pequeña en la primera película:", smallest_starship_in_first_movie())
