from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This serves your HTML file
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # This is where your logic happens
    user_input = request.form.get('user_data')
    
    # You can call any function or external script here
    result = f"Python processed your input: {user_input}"
    
    return f"<h1>Success!</h1><p>{result}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)