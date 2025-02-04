from flask import Flask, request, jsonify
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d**power for d in digits) == n

def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}")
    return response.text if response.status_code == 200 else "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    num = int(number)
    properties = ["odd" if num % 2 else "even"]
    
    if is_prime(num):
        properties.append("prime")
    if is_perfect(num):
        properties.append("perfect")
    if is_armstrong(num):
        properties.append("armstrong")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(map(int, str(num))),
        "fun_fact": get_fun_fact(num),
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
