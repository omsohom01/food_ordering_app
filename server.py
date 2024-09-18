from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Handle the order submission
@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Extract order details from the request
    data = request.json
    name = data.get('name')
    roll_number = data.get('roll_number')
    department = data.get('department')
    order_summary = data.get('order_summary')
    total_price = data.get('total_price')
    
    # Format the message to be displayed
    order_details = {
        "name": name,
        "roll_number": roll_number,
        "department": department,
        "order_summary": order_summary,
        "total_price": total_price
    }

    # Log the order details to the server console
    print("Order Details Received:")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Department: {department}")
    print(f"Order Summary: {order_summary}")
    print(f"Total Price: {total_price}")

    # Pass the order details to the client-side
    return jsonify(order_details)

if __name__ == '__main__':
    app.run(debug=True)
