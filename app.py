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


if __name__ == "__main__":
    print("server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
