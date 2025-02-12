from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class todo(db.Model):
    number = db.Column(db.Integer, primary_key=True)  # ID column (primary key)
    title = db.Column(db.String(80), nullable=False)  # Username column
    desc = db.Column(db.String(120), nullable=False)  # First name column
    

def __repr__(self):
        return f"<number={self.number}, title={self.title}, desc={self.desc}, Created At={self.created_at}>"

with app.app_context():
     db.create_all()
    


@app.route("/index")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
     app.run(debug=True)
