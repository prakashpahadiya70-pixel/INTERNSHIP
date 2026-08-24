from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type: ignore[import]

app = Flask(__name__)

# PostgreSQL Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/AI_Interns'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Intern(db.Model):
    __tablename__ = "interns"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    skills = db.Column(db.String(200))
    score = db.Column(db.Integer)
    domain = db.Column(db.String(100))

@app.route('/')
def home():
    interns = Intern.query.all()

    result = ""

    for i in interns:
        result += f"{i.id} | {i.name} | {i.skills} | {i.score} | {i.domain}<br>"

    return result

if __name__ == "__main__":
    app.run(debug=True)