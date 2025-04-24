import requests
from config import API_KEY

def get_info(country):
    api_url_country = f'https://api.api-ninjas.com/v1/country?name={country}'

    response = requests.get(api_url_country, headers={'X-Api-Key': API_KEY})


    if response.status_code == 200:
        data = response.json()
        if data:
            country_data = data[0]

            name = country_data.get("name", "No info")
            region = country_data.get("region", "No info")
            capital_сountry = country_data.get("capital", "No info")
            gdp = country_data.get("gdp", "No info")
            currency = country_data.get("currency", "No info")
            life_exp = country_data.get("life_expectancy_male", "No info")
            unemployment = country_data.get("unemployment", "No info")
            
            capital_short = capital_сountry.split(",")
            capital_city = capital_short[0]

            print("\nИнформация о стране: ")
            print(f"Название: {name}")
            print(f"Регион: {region}")
            print(f"Столица: {capital_сountry}")
            print(f"ВВП: {gdp}")
            print(f"Продолжительность жизни: {life_exp}")
            print(f"Безработица: {unemployment}")
            print(f"Деньги: Валюта {currency.get("code")}, Название {currency.get("name")}")


            if capital_city:
                get_info_capital(capital_city, name)
            else:
                print("No data about capital")

        else:
            print("error")
    else:
        print("error")




def get_info_capital(capital_city, country_name):
    api_url_city = f"https://api.api-ninjas.com/v1/city?name={capital_city}"

    response_city = requests.get(api_url_city, headers={'X-Api-Key': API_KEY})

    if response_city.status_code == 200:
        data_city = response_city.json()
        if data_city:
            city_data = data_city[0]

            city_name = city_data.get("name", "No info")
            city_latitude = city_data.get("latitude", "No info")
            city_population = city_data.get("population", "No info")


            print(f"\nИнформация о столице: {country_name}")
            print(f"Название: {city_name}")
            print(f"Широта: {city_latitude}")
            print(f"Популяция: {city_population}")
        else:
            print("error")
    else:
        print("error")


country = input("\nВведите название страны: ")
get_info(country)



