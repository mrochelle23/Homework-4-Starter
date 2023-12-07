from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

app = Flask(__name__)

############################################################
ca = certifi.where()
# get this path from the panel on mongodb.com
uri = "mongodb+srv://mikhairochelle:JMoL2Qkw0SOO1scg@cluster0.8vhapfy.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Get the database names plantsdatabase
db = client.plantTest

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)
############################################################
# SETUP
############################################################

app.config["MONGO_URI"] = "mongodb://localhost:27017/plantsDatabase"
mongo = PyMongo(app)


############################################################
# ROUTES
############################################################

@app.route('/')
def plants_list():
    """Display the plants list page."""

    # TODO: Replace the following line with a database call to retrieve *all*
    # plants from the Mongo database's `plants` collection.
    plants_data = db.plants.find()

    context = {
        'plants': plants_data
    }
    return render_template('plant_list.html', **context)

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Display the plant creation page & process data from the creation form."""
    if request.method == 'POST':
        # TODO: Get the new plant's name, variety, photo, & date planted, and
        # store them in the object below.
        new_plant = {
            'name': request.form['plant_name'],
            'variety': request.form['variety'],
            'photo_url': request.form['photo'],
            'date_planted':request.form['date_planted']
        }
        # TODO: Make an `insert_one` database call to insert the object into the
        # database's `plants` collection, and get its inserted id. Pass the
        # inserted id into the redirect call below.
        #insert = db.plants.insert_one({ name: 'Pansy' }) adds a new plant/record to the plants collection
        insert = db.plants.insert_one(new_plant)

        return redirect(url_for('detail', plant_id=insert.inserted_id))

    else:
        return render_template('create.html')

@app.route('/plant/<plant_id>')
def detail(plant_id):
    """Display the plant detail page & process data from the harvest form."""

    # TODO: Replace the following line with a database call to retrieve *one*
    # plant from the database, whose id matches the id passed in via the URL.
    plant_to_show = db.plants.find_one(plant_id)

    # TODO: Use the `find` database operation to find all harvests for the
    # plant's id.
    # HINT: This query should be on the `harvests` collection, not the `plants`
    # collection.
    harvests = db.harvests.find()

    context = {
        'plant' : plant_to_show,
        'harvests': harvests
    }
    return render_template('detail.html', **context)

@app.route('/harvest/<plant_id>', methods=['POST'])
def harvest(plant_id):
    """
    Accepts a POST request with data for 1 harvest and inserts into database.
    """

    # TODO: Create a new harvest object by passing in the form data from the
    # detail page form.
    quantity = request.form.get("e.g. 3 tomatoes")
    date_planted = request.form.get("date_planted")

    new_harvest = {
        'quantity': quantity, # e.g. '3 tomatoes'
        'date': date_planted,
        'plant_id': plant_id
    }

    # TODO: Make an `insert_one` database call to insert the object into the
    # `harvests` collection of the database.
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["harvests"]

    x = mycol.insert_one(new_harvest)

    return redirect(url_for('detail', plant_id=plant_id))

@app.route('/edit/<plant_id>', methods=['GET', 'POST'])
def edit(plant_id):
    """Shows the edit page and accepts a POST request with edited data."""

    if request.method == 'POST':
        # TODO: Make an `update_one` database call to update the plant with the
        # given id. Make sure to put the updated fields in the `$set` object.
        updated_data = {
            'name': request.form['plant_name'],
            'variety': request.form['variety'],
            'photo_url': request.form['photo'],
            'date_planned': request.form['date_planned']
        }

        db.plants.update_one(
            {'_id': ObjectId(plant_id)},
            {'$set': updated_data}
        )
        return redirect(url_for('detail', plant_id=plant_id))
    else:
        # TODO: Make a `find_one` database call to get the plant object with the
        # passed-in _id.
        plant_to_edit = db.plants.find_one(plant_id)
        return render_template('edit.html', plant=plant_to_edit)

@app.route('/delete/<plant_id>', methods=['POST'])
def delete(plant_id):
    # TODO: Make a `delete_one` database call to delete the plant with the given
    # id.
    db.plants.delete_one({'_id': ObjectId(plant_id)})
    # TODO: Also, make a `delete_many` database call to delete all harvests with
    # the given plant id.
    db.harvests.delete_many({'_id': ObjectId(plant_id)})

    return redirect(url_for('plants_list'))

if __name__ == '__main__':
    app.run(debug=True)

# JMoL2Qkw0SOO1scg
# mongodb+srv://mikhairochelle:JMoL2Qkw0SOO1scg@cluster0.8vhapfy.mongodb.net/?retryWrites=true&w=majority

#python -m pip install "pymongo[srv]"