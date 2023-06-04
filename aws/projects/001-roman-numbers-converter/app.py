from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_roman(number):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_number = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_number += numeral
            number -= value
    return roman_number

def validate_input(input_value):
    if not input_value:
        return False, 'Input cannot be empty.'
    try:
        number = int(input_value)
        if number < 1 or number > 3999:
            return False, 'Input must be a decimal number between 1 and 3999!'
    except ValueError:
        return False, 'Input must be a decimal number not string!'
    return True, ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_value = request.form['number']
        valid, error_message = validate_input(input_value)
        if valid:
            number = int(input_value)
            roman_number = convert_to_roman(number)
            return render_template('results.html', number=number, roman_number=roman_number, developer_name='Said')
        else:
            return render_template('results.html', error_message=error_message, developer_name='Said')
    return render_template('index.html', developer_name='Said')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=80)