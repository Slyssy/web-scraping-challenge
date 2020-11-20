# from mission_to_mars import scrape
from mars_scrape import scrape
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "The app is up!"

@app.route("/scrape")
def scrape_route(query):
    return(scrape)



if __name__ == "__main__":
    app.run(debug=True)


