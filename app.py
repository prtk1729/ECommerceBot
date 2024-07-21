from flask import jsonify, render_template, Flask, request
import os
from dotenv import load_dotenv

from ecombot.retrieval_and_generation import generation
from ecombot.ingest import ingest_data

app = Flask(__name__)

# store env vars
load_dotenv()

vstore = ingest_data("Done")
chain = generation(vstore)


# create a home route
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods = ["GET", "POST"])
def chat():
    userText = request.form["msg"]

    # incoke the chain to get the response
    response = chain.invoke(userText)
    return str(response)

if __name__ == "__main__":
    app.run(debug = True)
