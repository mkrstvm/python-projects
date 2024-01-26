from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def to_dict(self):
        return {column.name:getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=request.form.get('password')
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("secrets.html")
    return render_template("register.html")


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    return "Login post called"


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route("/users")
def get_user():
    results = db.session.execute(db.select(User))
    users = results.scalars().all()
    return jsonify(users=[user.to_dict() for user in users])


@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
