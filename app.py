from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to check if a number is Armstrong
def is_armstrong(number):
    digits = str(abs(number)).replace('.', '')  # Remove the decimal point
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == abs(number)

# Function to check if a number is prime
def is_prime(number):
    if abs(number) < 2:
        return False
    for i in range(2, int(abs(number) ** 0.5) + 1):
        if abs(number) % i == 0:
            return False
    return True

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Check if the number is a valid number (integer or float)
    try:
        number = float(number)  # Try to convert to a float
    except ValueError:
        return jsonify({"number": number, "error": True, "message": "Invalid number"}), 400

    # Initialize properties list
    properties = []

    # Check for Armstrong number
    if is_armstrong(number):
        properties.append("armstrong")

    # Check if the number is odd or even
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    
    # Calculate the digit sum (ignoring the decimal point if float)
    digit_sum = sum(int(digit) for digit in str(abs(number)) if digit.isdigit())

    # Example response with the requested structure
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": False,  # Not implementing perfect number logic, adjust if needed
        "properties": properties,  # Only "armstrong", "odd", or "even"
        "digit_sum": digit_sum,
        "fun_fact": f"Fun fact about {number}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
