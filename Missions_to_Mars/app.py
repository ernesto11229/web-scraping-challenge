from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars



app = Flask(__name__)

mongo = PyMongo(app,uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("indexm.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars_db
    data = scrape_mars.scrape()
    mars.update(
        {},
        data,
        upsert=True
    )
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)