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
    name = data['name']
    roll_number = data['roll_number']
    department = data['department']
    order_details = data['order_details']

    response_message = f"{order_details}Ordered by {name}, Roll No: {roll_number}, Department: {department}."
    print(response_message)  # Server logs the order
    return jsonify({"message": response_message})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
