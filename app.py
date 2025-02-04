from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to check if a number is Armstrong
def is_armstrong(number):
    digits = str(abs(number))  # Convert number to string to process each digit
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits if digit.isdigit())  # Ensure we only process digits
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

    # Try to convert to a float (to allow negative and float numbers)
    try:
        number = float(number)  # Convert to float for handling both integers and floats
    except ValueError:
        return jsonify({"error": True, "message": "Invalid number"}), 400

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

    # Calculate the sum of digits
    # This will ignore the decimal point and only sum digits
    number_str = str(abs(number)).replace('.', '')  # Remove the decimal point
    digit_sum = sum(int(digit) for digit in number_str if digit.isdigit())

    # Example response with the requested structure
    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": False,  # Not implementing perfect number logic, adjust if needed
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": f"Fun fact about {number}"
    })

if __name__ == '__main__':
    app.run(debug=True)
