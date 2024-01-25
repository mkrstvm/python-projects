import time
from flask import Flask, render_template
import requests


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def speed_decorator(func):
    def wrapper_fun():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} run speed = {end_time - start_time}s")

    return wrapper_fun


@speed_decorator
def func1():
    for i in range(10000):
        i * i


func1()
speed_decorator(func1)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/<username>")
def greet_user(username):
    username = username + 12
    return f"welcome {username}"


@app.route("/guess/<username>")
def guess_user(username):
    gender_rl = f"https://api.genderize.io?name={username}"
    gender_response = requests.get(gender_rl)
    gender = gender_response.json()["gender"]
    age_url = f"https://api.agify.io?name={username}"
    age_response = requests.get(age_url)
    age = age_response.json()["age"]
    return render_template("guess.html", username=username, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
