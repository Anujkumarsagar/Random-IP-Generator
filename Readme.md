

# IP Location Tracker 🌎

This Python script helps you track IP addresses and retrieve their location information using various methods.

## Features

- **IP Location Tracking:** Retrieve location information based on IP addresses.
- **Random IP Generation:** Generate random IP addresses for testing purposes.
- **Multitasking:** Use multitasking to continuously track IP locations.

## Dependencies

- `geopy`: For geocoding and reverse geocoding.
- `geocoder`: For retrieving location information based on IP addresses.
- `multitasking`: For running tasks concurrently.

## Installation

1. Clone the repository:
   ```bash
   https://github.com/Anujkumarsagar/Random-IP-Generator/new/main
   cd Random-IP-Generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Import the necessary libraries:
   ```python
   import random
   import multitasking
   from geopy.geocoders import Nominatim
   import geocoder
   ```

2. Run the script:
   ```bash
   python Random-ip.py
   ```

## Functions

### `get_location_from_ip(ip_address)`

Get location information based on an IP address.

### `gen_random_ip()`

Generate a random IP address.

### `get_location(latitude, longitude)`

Get location information based on latitude and longitude coordinates.

### `main()`

Main function to continuously track IP locations.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
```

Feel free to customize it further based on your preferences!
