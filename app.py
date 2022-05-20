
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
@app.route("/", methods = ["GET"])
def index_page():

    meal = Meal.query.all()

    return render_template("index.html", meal = meal)

@app.route("/addMeal")
def add_recipes():
    return render_template("add_meal.html")

@app.route("/searchMeal")
def search_Meal():
    return render_template("search_meal.html")



#adding recipes
@app.route("/add-recipes", methods = ["POST"])
def add_meal():

    name = request.form.get("recipesName")
    time = request.form.get("timerequired")
    ingredients = request.form.get("ingredients")
    description = request.form.get("instructions")

    meal = Meal(name = name, time = time, ingredients=ingredients,description= description) # meal object
    db.session.add(meal)
    db.session.commit() # save to database


    #if error occurs return to the main page
    return redirect("/")

@app.route("/search-recipes",methods = ["POST"])
def searchMeal():

    search= request.form.get("searchitem")
    print(search)

    return redirec("/")



@app.route("/delete/<meal_id>",methods = ["GET"])
def delete_meal(meal_id):

    meal = Meal.query.get(int(meal_id))

    db.session.delete(meal)
    db.session.commit()



    return redirect("/")






#run the app
if __name__ == "__main__":
    app.run()
