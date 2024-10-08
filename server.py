from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__)

# Serve index.html from the root directory
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static images from the 'images' folder
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

# Endpoint to handle order submissions
@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json
    name = data['name']
    roll_number = data['roll_number']
    department = data['department']
    order_summary = data['order_summary']
    total_bill = data['total_bill']

    # Print the submitted details to the console
    print(f"Received Order Details:")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Department: {department}")
    print(f"Order Summary: {order_summary}")
    print(f"Total Bill: Rs {total_bill}")

    # Response message to be sent back to the client
    response_message = (
        f"Order Summary:<br>{order_summary}<br>"
        f"Total Bill: Rs {total_bill}<br>"
        f"Customer Name: {name}<br>"
        f"Roll Number: {roll_number}<br>"
        f"Department: {department}"
    )

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
