from mars_scrape import scrape
from mars_scrape import configure_firefox_driver
from flask import Flask, jsonify
import pymongo
import os


CONN = os.getenv()
client = pymongo.MongoClient(CONN)
db = client.mars


driver = configure_firefox_driver()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("CONN")

mongo_client = PyMongo(app)

@app.route("/")
def main():
    return "The app is up!"

@app.route("/scrape")
def scrape_route():
    db.mars.insert_one(scrape(driver)) 
    db.mars.drop()
    return (scrape)

# @app.route("/all")
# def all_data()

if __name__ == "__main__":
    app.run(debug=True)


