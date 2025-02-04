from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def is_armstrong(number):
    # Ensure the number is an integer
    if not isinstance(number, int):
        return False
    digits = str(abs(number))
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == abs(number)

def is_prime(number):
    # Handle both integer and float inputs
    if isinstance(number, float):
        if not number.is_integer():
            return False
        number = int(number)
    number = abs(number)
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_input = request.args.get('number')

    # Validate and convert input
    try:
        number_float = float(number_input)
    except ValueError:
        # Return original invalid input in 'number' field
        return jsonify({
            "error": True,
            "message": "Invalid number",
            "number": number_input  # Include original input
        }), 400

    properties = []
    is_integer = number_float.is_integer()
    number_int = int(number_float) if is_integer else None

    # Check Armstrong (only for integers)
    if is_integer and is_armstrong(number_int):
        properties.append("armstrong")

    # Check Odd/Even (only for integers)
    if is_integer:
        properties.append("odd" if number_int % 2 != 0 else "even")

    # Sum of digits (ignore decimal points)
    number_str = str(abs(number_float)).replace('.', '')
    digit_sum = sum(int(digit) for digit in number_str if digit.isdigit())

    # Prime check (handled in is_prime)
    prime_check = is_prime(number_float)

    return jsonify({
        "number": number_float,
        "is_prime": prime_check,
        "is_perfect": False,  # Placeholder as per original code
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": f"Fun fact about {number_float}"
    })

if __name__ == '__main__':
    app.run(debug=True)