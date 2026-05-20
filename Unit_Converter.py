from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('length.html')

@app.route('/length', methods=['GET', 'POST'])
def length():

    result = None
    if request.method == 'POST':

        value = float(request.form['length_value'])
        unit_current = request.form['length_units_from']
        unit_convert_to = request.form['length_units_to']
        convert_to_meter = {'millm':value/1000, 'centm':value/100, 'meter':value, 'kilom':value*1000, 'inch':value/39.37, 'foot':value/3.281, 'yard':value/1.094, 'mile':value*1609}
        value = convert_to_meter[unit_current]
        convert_from_meter = {'millm':value*1000, 'centm':value*100, 'meter':value, 'kilom':value/1000, 'inch':value*39.37, 'foot':value*3.281, 'yard':value*1.094, 'mile':value/1609}
        result = round(convert_from_meter[unit_convert_to], 2) 

    return render_template('length.html', result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():

    result = None
    if request.method == 'POST':

        value = float(request.form['weight_value'])
        unit_current = request.form['weight_units_from']
        unit_convert_to = request.form['weight_units_to']
        convert_to_gram = {'millg':value/1000, 'gram':value, 'kilog':value*1000, 'metric_ton':value*1000000, 'grain':value/15.432, 'ounce':value*28.35, 'pound':value*453.6, 'short_ton':value*907200}
        value = convert_to_gram[unit_current]
        convert_from_gram = {'millg':value*1000, 'gram':value, 'kilog':value/1000, 'metric_ton':value/1000000, 'grain':value*15.432, 'ounce':value/28.35, 'pound':value/453.6, 'short_ton':value/907200}
        result = round(convert_from_gram[unit_convert_to], 2)

    return render_template('weight.html', result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():

    result = None
    if request.method == 'POST':
        
        value = float(request.form['temperature_value'])
        unit_current = request.form['temperature_units_from']
        unit_convert_to = request.form['temperature_units_to']
        convert_to_celsius = {'celsius':value, 'fahrenheit':(value-32)*5/9, 'kelvin':value-273.15}
        value = convert_to_celsius[unit_current]
        convert_from_celsius  = {'celsius':value, 'fahrenheit':(value*9/5)+32, 'kelvin':value+273.15}
        result = round(convert_from_celsius [unit_convert_to], 2) 

    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
