# Unit Converter

A simple web application built with Python and Flask that converts between different units of measurement. https://roadmap.sh/projects/unit-converter

## Features

- **Length:** millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
- **Weight:** milligram, gram, kilogram, metric ton, grain, ounce, pound, short ton
- **Temperature:** Celsius, Fahrenheit, Kelvin

## Usage

1. Install dependencies:
```bash
pip install flask
```

2. Run the application:
```bash
python Unit_Converter.py
```

3. Open your browser and go to `http://127.0.0.1:5000/`

## How it works

The user inputs a value, selects the unit to convert from and to, and submits the form. Flask receives the data, performs the conversion on the backend, and displays the result on the same page.

## Requirements

- Python 3.10+
- Flask
