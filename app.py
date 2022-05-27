
from flask import Flask,render_template,request, redirect, flash#
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

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

#for adding meal page
@app.route("/addMeal")
def add_recipes():
    return render_template("add_meal.html")

#for searching meals page
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

    meal=Meal.query.filter(Meal.name ==name).all()
    


    #if error occurs return to the main page
    return render_template("add_meal.html", meal=meal)

#searching meth
@app.route("/search-recipes",methods = ["POST"])
def searchMeal():

    search= request.form.get("searchitem")
    serachOption=request.form.get("searchoption")

    print(search)
    print(serachOption)

    meal1 = None
    
    if serachOption == "name":
        a=Meal.query.filter(Meal.name.ilike(search)).all()
        meal1 = a
       # print(a)
    if serachOption == "time":
        a=Meal.query.filter(Meal.time <=int(search)).all()
        meal1= a
       # print(a)

    if serachOption == "ingredients":
        a=Meal.query.filter(Meal.ingredients.contains(search)).all()
        meal1=a
        #print(a)

    print(meal1)

    

    return render_template("search_meal.html", meal1 = meal1)
   


#deleteing meals
@app.route("/delete/<meal_id>",methods = ["GET"])
def delete_meal(meal_id):

    #get the meal
    meal = Meal.query.get(int(meal_id))

    db.session.delete(meal) #delete the meal
    db.session.commit()



    return redirect("/")



#run the app
if __name__ == "__main__":
    app.run()
