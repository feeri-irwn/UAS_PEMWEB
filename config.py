from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

#init db connect
app = Flask(__name__)
CORS(app,resources={r"/api/*": {"origins": "*"}},supports_credentials=True)
#CORS(app, origins=["http://localhost:5173"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://feri-sql:1234@localhost:3306/uas-sql'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://uassql_doesvapor:2561f8d0054c0561451c32aa271481d17d7675cc@x7v16.h.filess.io:3306/uassql_doesvapor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "hello world!!!"
app.app_context().push()