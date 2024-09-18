from flask import Flask, send_from_directory, jsonify, request
import os

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
    order_summary = data['order_summary']
    name = data['name']
    roll_number = data['roll_number']
    department = data['department']
    total_price = data['total_price']

    response_message = f"Order Summary:<br>{order_summary}<br><strong>Name:</strong> {name}<br><strong>Roll Number:</strong> {roll_number}<br><strong>Department:</strong> {department}<br><strong>Total Bill:</strong> ₹{total_price}/-"
    print(response_message)  # Server logs the order
    return jsonify({"message": response_message})

if __name__ == '__main__':
    # Ensure the app listens on the port specified by Render
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
