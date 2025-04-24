import asyncio
import aiohttp
import aioconsole
from config import API_KEY


async def preload_country_data(session, country):
    api_url_country = f'https://api.api-ninjas.com/v1/country?name={country}'
    async with session.get(api_url_country, headers={'X-Api-Key': API_KEY}) as response:
        if response.status == 200:
            data = await response.json()
            return data[0] if data else None
        return None
    
async def preloaded_city_data(session, city):
    api_url_city = f'https://api.api-ninjas.com/v1/city?name={city}'
    async with session.get(api_url_city, headers={'X-Api-Key': API_KEY}) as response:
        if response.status == 200:
            data = await response.json()
            return data[0] if data else None
        return None

async def get_info():

    countries = ["United States", "Russia", "Germany", "Japan", "France", "South Africa", "Brazil", "Argentina", "Vietnam", "Egypt"]

    prelodaded_data = {}

    async with aiohttp.ClientSession() as session:
        get_data = [preload_country_data(session,country) for country in countries]
        result = await asyncio.gather(*get_data)

        for country, data in zip(countries, result):
            if data:
                prelodaded_data[country] = data
                print(f"Данные о {country} получены заранее")

        user_country = await aioconsole.ainput("\nВведите название страны: ")

        country_data = None
        if user_country in prelodaded_data:
            print(f"Используем заранее загруженные данные о стране {user_country}")
            country_data = prelodaded_data[user_country]
        else:
            print(f"Загружаем данные о стране {user_country}")
            country_data = await preload_country_data(session, user_country)

        if country_data:

            name = country_data.get("name")
            region = country_data.get("region")
            capital_сountry = country_data.get("capital")
            gdp = country_data.get("gdp")
            currency = country_data.get("currency")
            life_exp = country_data.get("life_expectancy_male")
            unemployment = country_data.get("unemployment")
            
            print("\nИнформация о стране: ")
            print(f"Название: {name}")
            print(f"Регион: {region}")
            print(f"Столица: {capital_сountry}")
            print(f"ВВП: {gdp}")
            print(f"Продолжительность жизни: {life_exp}")
            print(f"Безработица: {unemployment}")
            print(f"Деньги: Валюта {currency.get("code")}, Название {currency.get("name")}")


            if capital_сountry:
                capital_short = capital_сountry.split(",")
                capital_city = capital_short[0]
                city_data = await preloaded_city_data(session, capital_city)

                if city_data:
                    city_name = city_data.get("name")
                    city_latitude = city_data.get("latitude")
                    city_population = city_data.get("population")


                    print(f"\nИнформация о столице страны: {user_country}")
                    print(f"Название: {city_name}")
                    print(f"Широта: {city_latitude}")
                    print(f"Популяция: {city_population}")
                else:
                    print(f"Нет информации о столице {capital_сountry}")
        else:
            print(f"Нет информации о стране {user_country}")


asyncio.run(get_info())
