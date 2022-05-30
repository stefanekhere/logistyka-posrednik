from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
from flask import jsonify


app = Flask(__name__)
app.debug = True
app.config["CACHE_TYPE"] = "null"


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/calculate", methods=["POST"])
def dane():
    print(request.form.getlist('odbiorca'))
    dataToReturn = [[1,2,3],[2,3,4]]
    return jsonify(dataToReturn)
    return request.form['odbiorca'][2]
