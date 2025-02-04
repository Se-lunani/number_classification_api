from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Check if the number is a valid number (integer or float)
    try:
        number = float(number)  # Try to convert to a float
    except ValueError:
        return jsonify({"error": True, "message": "Invalid number"}), 400

    # If the number is valid, continue with processing
    # Add your logic here to classify the number and return a response
    is_prime = False  # You can add your logic for prime check
    is_perfect = False  # You can add your logic for perfect number check
    properties = []
    digit_sum = sum(int(digit) for digit in str(abs(number)) if digit.isdigit())

    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    
    # Add additional checks for Armstrong numbers or other properties
    # Example response
    return jsonify({
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": f"Fun fact about {number}"
    })

if __name__ == '__main__':
    app.run(debug=True)
