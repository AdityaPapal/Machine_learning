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




if __name__ == "__main__":
    app.run(debug= True)