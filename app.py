from mars_scrape import scrape
from mars_scrape import configure_firefox_driver
from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
import os




driver = configure_firefox_driver()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("CONN")

mongo_client = PyMongo(app, connect=False)

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    mars_data = list(mongo_client.db.mars.find())
    print(mars_data)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape_route():
    mongo_client.db.mars.drop()
    mongo_client.db.mars.insert_one(scrape(driver)) 
    return redirect("/", code=303)



if __name__ == "__main__":
    app.run(debug=True)


