from flask import Flask, request

app = Flask(__name__)

@app.route('/bienvenido', methods=['GET'])
def bienvenido():
    return "Hola mundo"

if __name__ == '__main__':
    app.run()