# Weather CLI

This is a command-line interface (CLI) application for retrieving weather information for a specified city using the OpenWeatherMap API. 

## Installation

1. Clone this repository to your local machine.
2. Install the required packages using `pip`:
```
pip install requests click
```
3. Obtain an API key from OpenWeatherMap and replace `your_api_key_here` with your actual API key in `weather.py`.

## Usage

To use this CLI application, run the `weather.py` script in the terminal and enter the name of a city when prompted:
```
python weather.py
```

The CLI will retrieve weather information from the OpenWeatherMap API and display the current temperature and weather description for the specified city.

## Example

```
$ python weather.py
Enter city name: San Francisco
Temperature in San Francisco: 15 C
Weather description: clear sky
```

## Dependencies

This CLI application requires the following Python packages:

- `requests`
- `click`

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.
