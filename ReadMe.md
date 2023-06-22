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

## Update History

### Version 1.1
In this updated code::

- Error Handling: The `make_api_request` function now raises an exception if the response status code is not 200. The `get_weather` function handles this exception and logs an error message.
- Input Validation: Input validation is not explicitly performed in this code snippet. However, the OpenWeatherMap API will respond with an appropriate error if an invalid city name is provided.
- API Key Handling: The API key is retrieved from an environment variable using `os.getenv`. Make sure to set the `OPENWEATHERMAP_API_KEY` environment variable with your actual API key.
- Unit Testing: While unit testing is not included in this code snippet, it is recommended to write unit tests for functions like `make_api_request`, `parse_weather_data`, and `display_weather` to verify their behavior under different scenarios.
- Modularity: The code has been organized into separate functions for making the API request, parsing the response, and displaying the weather information. This improves code readability, testability, and reusability.
- Logging: Logging has been incorporated using the logging module. The log messages are written to a file specified by `LOG_FILE`. The logging level is set to INFO, but you can adjust it as needed.

Remember to set the `OPENWEATHERMAP_API_KEY` environment variable with your actual API key before running the script.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.txt](LICENSE.txt) file for details.
