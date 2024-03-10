# task_1
# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests

def download_and_save_robots_txt(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as file:
        file.write(response.text)

download_and_save_robots_txt('https://www.wikipedia.org/robots.txt', 'wikipedia_robots.txt')
download_and_save_robots_txt('https://www.twitter.com/robots.txt', 'twitter_robots.txt')

# task_3
#Write a console application which takes as an input a city name and returns current weather
# in the format of your choice.
# For the current task, you can choose any weather API or website or use openweathermap.org

import requests

def get_weather(city_name):
    api_key = "aecd63cc3ea359ddf854c9efa37cd701"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["weather"][0]["description"]

city_name = input("Write the city name: ")
print(f"The weather in {city_name}: {get_weather(city_name)}")
