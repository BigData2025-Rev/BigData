from flask import Flask, request

app: Flask = Flask(__name__) #this tells flask where to look for resources (name is reference to the module it resides in)

count = 0

data_set = {"1":"some data","2":"more data"} # we will use with query route later

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World"

@app.route("/greeting/<name>", methods=["GET"])
def greeting(name: str):
    return f"Hello {name}"

@app.route("/<num1>/add/<num2>", methods = ["GET"])
def addition(num1: str, num2: str):
    result = int(num1) + int(num2)
    return str(result)

@app.route("/login", methods=["POST"])
def login():
    credentials = request.get_json() #sets out variable to the JSON dictionary values
    username = credentials["username"]
    password = credentials["password"]
    if username == "good" and password == "correct":
        return "your credentials are good!"
    else:
        return "your credentials are bad!"

@app.route("/count",methods = ["PATCH"])
def add_count():
    global count
    count +=1
    return f"The count is now {count}"

@app.get("/data") # route will look like this: http://domain:port/data?query_param=value
def query_database():
    query = request.args["DB"]
    if query =="":
        return data_set
    else:
        return data_set[query]

app.run()
