from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello Sudhir!</h1>
    <h2>Welcome to Simple Calculator</h2>
    <div style="border: 2px solid #333; padding: 20px; max-width: 400px; border-radius: 8px; background-color: #f0f0f0;">
        <h3>Calculator Operations</h3>
        <form action="/calculate" method="GET" style="display: flex; flex-direction: column; gap: 10px;">
            <input type="number" name="num1" placeholder="Enter first number" required style="padding: 8px; font-size: 16px;">
            <select name="operation" required style="padding: 8px; font-size: 16px;">
                <option value="">Select Operation</option>
                <option value="add">+ (Addition)</option>
                <option value="subtract">- (Subtraction)</option>
                <option value="multiply">* (Multiplication)</option>
                <option value="divide">/ (Division)</option>
            </select>
            <input type="number" name="num2" placeholder="Enter second number" required style="padding: 8px; font-size: 16px;">
            <button type="submit" style="padding: 10px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">Calculate</button>
        </form>
    </div>
    """

@app.route("/calculate")
def calculate():
    from flask import request
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')
        
        if operation == 'add':
            result = num1 + num2
            op_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            op_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            op_symbol = '*'
        elif operation == 'divide':
            if num2 == 0:
                return "<h2>Error: Cannot divide by zero!</h2><a href='/'>Back to Calculator</a>"
            result = num1 / num2
            op_symbol = '/'
        else:
            return "<h2>Invalid operation</h2><a href='/'>Back to Calculator</a>"
        
        return f"""
        <h1>Calculator Result</h1>
        <h2>{num1} {op_symbol} {num2} = {result}</h2>
        <a href='/' style="padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 4px;">Back to Calculator</a>
        """
    except:
        return "<h2>Error in calculation</h2><a href='/'>Back to Calculator</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)