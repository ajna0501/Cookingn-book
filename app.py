
from flask import Flask,render_template,request, redirect#
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)

class Meal(db.Model):
    #table
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    time = db.Column(db.String)
    ingredients = db.Column(db.String)
    description = db.Column(db.String)


 #create database
db.create_all()


#langing page
@app.route("/")
def index_page():
    return render_template("index.html")

#adding recipes
@app.route("/add-recipes", methods = ["POST"])
def add_meal():

    name = request.form.get("recipesName")
    time = request.form.get("timerequired")
    ingredients = request.form.get("ingredients")
    description = request.form.get("instructions")

    meal = Meal(name = name, time = time, ingredients=ingredients,description= description)
    db.session.add(meal)
    db.session.commit()




    #if error occurs return to the main page
    return redirect("/")





#run the app
if __name__ == "__main__":
    app.run()
