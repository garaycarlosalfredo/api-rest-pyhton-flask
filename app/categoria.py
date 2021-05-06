from flask import Flask, jsonify

app = Flask (__name__)

@app.route('/', methods = ['GET'])

def index():
    return jsonify({'mensaje' : 'Bienvenido pyhton'})

if __name__ == '__main__':
    app.run(debug = True)
    #