import click
import requests

API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@click.command()
@click.option('--city', prompt='Enter city name', help='Name of the city for weather information')
def get_weather(city):
    """
    Retrieve weather information for a specified city.
    """
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        click.echo('Error retrieving weather data.')
        return

    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    click.echo(f'Temperature in {city}: {temperature} C')
    click.echo(f'Weather description: {description}')

if __name__ == '__main__':
    get_weather()
