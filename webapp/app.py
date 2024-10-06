from flask import Flask, request, jsonify, render_template_string


app = Flask(__name__)

@app.route('/')
def home():
    return  render_template_string('''
        <h1>Welcome to the Home Page</h1>
        <button onclick="gotosubtraction()">Subtraction</button>
        <button onclick="gotodivision()">Division</button>
        <br>
<body>

    <label for="num1">First Number to Add: </label>
    <input type="number" id="num1" placeholder="Enter first number">
    <br>
    <label for="num2">Second Number: </label>
    <input type="number" id="num2" placeholder="Enter second number">
    <br>
    <button onclick="addNumbers()" id="add">Add</button>

    <div id="result"></div>

    <script>
        function addNumbers() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const sum = num1 + num2;

            document.getElementById('result').innerText = `Result: ${sum}`;
        }
        function gotosubtraction(){
            window.location.href = "/subtraction";
        }
        function gotodivision(){
            window.location.href = "/division";
        }
    </script>

</body>
    ''')

@app.route('/', methods=['POST'])
def add_numbers():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    return jsonify(result=num1 + num2)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/subtraction')
def subtraction():
    return render_template_string('''
        <h1>Welcome to the Subtraction Page</h1>
        <button onclick="gotohomepage()">Go Home</button>
        <button onclick="gotodivision()">Division</button>
        <br>
<body>
    <label for="num1">First Number to Subtract: </label>
    <input type="number" id="num1" placeholder="Enter first number">
    <br>
    <label for="num2">Second Number: </label>
    <input type="number" id="num2" placeholder="Enter second number">
    <br>
    <button onclick="subtractNumbers()">Subtract</button>
    <br>
    <div id="result"></div>

    <script>
        function subtractNumbers() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const difference = num1 - num2;

            document.getElementById('result').innerText = `Result: ${difference}`;
        }
        function gotohomepage(){
            window.location.href = "/";
        }
        function gotodivision(){
            window.location.href = "/division";
        }
    </script>
    ''')

@app.route('/subtraction', methods=['POST'])
def subtract_numbers():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    return jsonify(result=num1 - num2)

@app.route('/division')
def division():
    return render_template_string('''
        <h1>Welcome to the Division Page</h1>
        <button onclick="gotohomepage()">Go Home</button>
        <button onclick="gotosubtraction()">Subtraction</button>
        <br>
<body>
    <label for="num1">First Number to Divide: </label>
    <input type="number" id="num1" placeholder="Enter first number">
    <br>
    <label for="num2">Second Number: </label>
    <input type="number" id="num2" placeholder="Enter second number">
    <br>
    <button onclick="divideNumbers()">Divide</button>
    <br>
    <div id="result"></div>

    <script>
        function divideNumbers() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const quotient = num1 / num2;

            document.getElementById('result').innerText = `Result: ${quotient}`;
        }
        function gotohomepage(){
            window.location.href = "/";
        }
        function gotosubtraction(){
            window.location.href = "/subtraction";
        }
    </script>
    ''')

@app.route('/division', methods=['POST'])
def divide_numbers():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    return jsonify(result=num1 / num2)
