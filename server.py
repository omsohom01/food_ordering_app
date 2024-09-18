from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Serve the HTML file from the root directory
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Handle the POST request for order submission
@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json
    name = data.get('name')
    roll_number = data.get('roll_number')
    department = data.get('department')
    order_summary = data.get('order_summary')
    total_price = data.get('total_price')
    
    # Log the order details
    print(f"Order received from {name} ({roll_number}), Department: {department}")
    print(f"Order Details: {order_summary}")
    print(f"Total Price: {total_price}")

    # Return the details as JSON
    return jsonify({
        'order_summary': order_summary,
        'name': name,
        'roll_number': roll_number,
        'department': department,
        'total_price': total_price
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
