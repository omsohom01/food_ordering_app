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
    food_item = data['food_item']
    name = data['name']
    roll_number = data['roll_number']
    department = data['department']
    quantity = data['quantity']

    response_message = f"{quantity} {food_item}(s) ordered by {name}, Roll No: {roll_number}, Department: {department}."
    print(response_message)  # Server logs the order
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
