from flask import flask, request
app = Flask(__name__)
@app.route('/hello')
def hello():
    return 'Hello, World!'
if __name__ == '__main__':    app.run(debug=True)
app.route('/greet', methods=['POST'])   
def greet():
    name = request.form.get('name', 'Guest')
    return f'Hello, {name}!'
if __name__ == '__main__':
    app.run(debug=True)
