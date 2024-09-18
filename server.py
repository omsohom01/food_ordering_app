from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    # Process order
    print(f"Received order: {data}")
    return jsonify({"message": "Order received!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
