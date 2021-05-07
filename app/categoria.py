from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init_(self,cat_nom,cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

db.create_all()



#Mensaje del index
@app.route('/', methods = ['GET'])

def index():
    return jsonify({'mensaje' : 'Bienvenido pyhton'})

if __name__ == '__main__':
    app.run(debug = True)
    #
