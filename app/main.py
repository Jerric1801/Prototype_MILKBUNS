from logging import error
from flask import Flask, jsonify, request, render_template
import os
from .predict import prediction
from .blockchain import Blockchain
import json


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

#login page
@app.route("/")
def login():

    return render_template('index.html.j2')

@app.route("/results")
def results():

    return render_template('results.html.j2')

@app.route("/blockchain")
def blockchain():
    with open("./app/static/get_chain.json", "r") as f:
        json_data = json.load(f)

    kwargs =  {"dictionary_list": json_data["chain"]}
    
    return render_template('blockchain.html.j2', **kwargs)

@app.route("/updateBlock", methods = ["POST"])
def updateBlock():
    if request.method == "POST":
        query = request.json
        blockObj = Blockchain()
        supplier = query["supplier"]
        cargo = query["cargo"]
        amount = query["amount"]
        destination = query["destination"]
        block = blockObj.create_blockchain(supplier, cargo, amount, destination,1 , '0')
        # Open the JSON file
        with open("./app/static/get_chain.json", "r") as f:
            json_data = json.load(f)

        # Add a new dictionary to the back of the list
        json_data["chain"].append(block)
        json_data["length"] = json_data["length"] + 1
        # Write the updated JSON data to the file
        with open("./app/static/get_chain.json", "w") as f:
            json.dump(json_data, f, indent=4)

        return jsonify("success")


@app.route("/predict", methods = ["POST"], strict_slashes = False)
def predict():
    if request.method == "POST":
        query = request.json
        result = prediction(query)
        return jsonify(result)
    

@app.route("/loadKey", methods=["GET"])
def load_key():
    api_key = os.environ.get('KEY', None)

    return jsonify(api_key)


