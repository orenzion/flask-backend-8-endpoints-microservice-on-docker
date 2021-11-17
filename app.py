from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 3200

# We use the INTO dict below to 'play' with data using different http request types

INFO = {
    "languages": {
        "es": "Spanish",
        "en": "English",
        "fr": "French"
    },
    "colors": {
        "r": "red",
        "g": "green",
        "b": "blue"
    },
    "clouds": {
        "IBM": "IBM CLOUD",
        "AMAZON": "AWS",
        "MICROSOFT": "AZURE"
    }
}


# GET METHOD
@app.route("/")
def home():
    return "<h1 style='color:blue'>This Is Home!</h1>"


# renter template from templates folder
@app.route("/temp")
def template():
    return render_template('index.html')


# return query string parameters added to the url
@app.route('/qstr')
def query_string():
    if request.args:
        args = request.args
        res = {}
        for key, value in args.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
    return res


# return INFO as a json
@app.route('/json')
def get_json():
    res = make_response(jsonify(INFO), 200)
    return res


# get member from a collection
@app.route("/json/<collection>/<member>")
def get_data(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res": member}), 200)
            return res

        res = make_response(jsonify({"error": "member not sound"}), 400)
        return res
    res = make_response(jsonify({"error": "collection not sound"}), 400)
    return res


# add new members to a collecition in INFO
@app.route("/json/<collection>", methods=['POST'])
def create_collection(collection):
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({"error": "collection already exists"}))
        return res

    INFO.update({collection: req})
    res = make_response(jsonify({"message": "collection added"}), 201)
    return res


# update an existing member in a collection, put method
@app.route("/json/<collection>/<member>", methods=['PUT'])
def update_collection(collection, member):
    req = request.get_json()

    if collection:
        if member:
            INFO[collection][member] = req['new']
            res = make_response(jsonify({"message": INFO[collection]}), 200)
            return res

        res = make_response(jsonify({"error": "member not found"}), 400)
        return res

    res = make_response(jsonify({"error": "collection not found"}), 400)
    return res


# delete a collection
@app.route("/json/<collection>", methods=['DELETE'])
def delete_collection(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO), 200)
        return res

    res = make_response(jsonify({"error": "collection not found"}), 400)
    return res


if __name__ == "__main__":
    print("server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
