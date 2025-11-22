import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask import jsonify
from sqlalchemy.testing.config import ident

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

api = "https://documenter.getpostman.com/view/49384540/2sB3QQK7vy"

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # Method 1
    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #
    #     # Put some properties in a sub-category
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # })

    # Method 2
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars()
    return jsonify(cafes=[cafe.to_dict()for cafe in all_cafes ])


@app.route("/search/<location>")
def search_location(location):
    # location= request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafe=[cafe.to_dict()for cafe in all_cafes])
    else:
        return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location."})

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    data = request.get_json()
    print(data)  # ✅ To confirm JSON

    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=data["has_toilet"],
        has_wifi=data["has_wifi"],
        has_sockets=data["has_sockets"],
        can_take_calls=data["can_take_calls"],
        coffee_price=data["coffee_price"]
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch(cafe_id):
    new_price= request.args.get("new_price")
    cafe_to_update = db.session.get(entity= Cafe, ident=cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()

        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error ={"Not found":"Sorry a cafe with that id was not found"})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    if api_key== "MoneyTrees":
        try:
            cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        except AttributeError:
            return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"})
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200

    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."})



if __name__ == '__main__':
    app.run(debug=True)
