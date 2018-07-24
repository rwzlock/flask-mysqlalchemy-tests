import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@127.0.0.1:3306/db" 

db = SQLAlchemy(app)


class Test(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(30))

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return '<Test %r>' % (self.name)

# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

    test1 = Test(name="Ryan", age=24, email="rwzlock@gmail.com")
    test2 = Test(name="Phil", age=24, email="phil222@gmail.com")
    test3 = Test(name="Tom", age=23, email="tjs219@lehigh.edu")

    db.session.add(test1)
    db.session.add(test2)
    db.session.add(test3)

    db.session.commit()

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    #test = Test(name="Giles", age=23, email="pokechu5@gmail.com")

    #db.session.add(Test)
    #db.session.commit()

    return render_template("index.html")

@app.route("/json")
def database():
    """Json."""
    
    results = db.session.query(Test.name, Test.age).all()

    name = [result[0] for result in results]
    age = [int(result[1]) for result in results]

    plot_trace = {
        "x": name,
        "y": age,
        "type": "bar"
    }
    return jsonify(plot_trace)

@app.route("/insert", methods=["GET","POST"])
def insert():
    """Json."""
    if request.method == 'POST':
        print(request)

        if request.files.get('text'):
            # read the file
            file = request.files['file']

            # read the filename
            filename = file.filename

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Image Saved!"
    test = Test(name="Giles", age=23, email="pokechu5@gmail.com")
    db.session.add(test)
    db.session.commit()

    return render_template("form.html")
    
if __name__ == '__main__':
    app.run(debug=True)