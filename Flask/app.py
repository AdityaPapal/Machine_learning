from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World</h1>"


@app.route('/a',methods = ['post'])
def operation():
    if (request.method == 'post'):
        firstname = request.json['first_name']
        lastname = request.json['last_name']
        result = f"My name is {firstname + lastname}"
    return jsonify(result)

@app.route('/b',methods = ["post"])
def add():
    if (request.method == "post"):
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        #result1 = f"Addition of two number is {num1+num2}"
    return jsonify( f"Addition of two number is {num1+num2}")


if __name__ == "__main__":
    app.run(debug= True)