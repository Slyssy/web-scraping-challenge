from mars_scrape import scrape
from mars_scrape import configure_firefox_driver
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os

driver = configure_firefox_driver()

# CONN=mongodb+srv://slyssy:wnfY23SMqATuZjTD@cluster0.na11p.mongodb.net/<dbname>?retryWrites=true&w=majority

app = Flask(__name__)
# app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# mongo_client = PyMongo(app)

@app.route("/")
def main():
    return "The app is up!"

@app.route("/scrape")
# mongo_client.db.mars.insert_many(scrape)
def scrape_route():
    return (scrape)

# @app.route("/all")
# def all_data()

if __name__ == "__main__":
    app.run(debug=True)


