import csv
import datetime
import requests

from flask import Flask, render_template, request, session
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://mans:flask@localhost/mans')
db = scoped_session(sessionmaker(bind=engine))


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

WEATHER_TOKEN = '1e35d2f152ba4f4f8e0175010202109'

@app.route("/")
def about():
    return render_template("about.html")



def weather_by_city():
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': WEATHER_TOKEN,
        'q': 'Grozny, Russia',
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }
    result = requests.get(weather_url, params=params)
    return result.json()

@app.route("/weather", methods=["GET","POST"])
def weather():
    weather = weather_by_city()
    degrees = {
        9: weather['data']['weather'][0]['hourly'][3]['tempC'],
        12: weather['data']['weather'][0]['hourly'][4]['tempC'],
        15: weather['data']['weather'][0]['hourly'][5]['tempC'],
        18: weather['data']['weather'][0]['hourly'][6]['tempC'],
        21: weather['data']['weather'][0]['hourly'][7]['tempC']
    }
    day = weather[ 'data']['weather'][0]['date']
    msg = f'Сегодня {day} погода ожидается следующая: в 9:00 {degrees[9]}°C,\
        в 12:00 {degrees[12]}°C в 15:00 {degrees[15]}°C, в 18:00 {degrees[18]}°C, в 21:00 {degrees[21]}°C'
    time = time=datetime.datetime.strptime('09:12AM', '%I:%M%p').time()
    return render_template( "weather.html", text=msg, time=time)


@app.route("/hello", methods=["POST"])
def hello():
    take = request.form.get("name")
    text = take
    with open('text.txt', 'w', encoding="utf-8") as txt_file:
        txt_file.write(text)
    return render_template("hello.html", message=take)


@app.route("/index", methods=["GET","POST"])
def index():
    if session.get('notes') is None:
        session['notes'] = []
    if request.method == "POST":
        note = request.form.get("note")
        comment = note
        session['notes'].append(note)
        with open('comment.txt', 'w', encoding="utf-8") as comment_file:
            comment_file.write(comment)
        f = open("comment.txt")
        reader = csv.reader(f)
        for origin in reader:
            db.execute("INSERT INTO flights (origin) VALUES (:origin)",
                        {"origin":origin})
        db.commit()   
    return render_template("index.html", notes=session['notes'])


# @app.route("/hello", methods=["POST"])
# def hello():
#     f = open("text.txt")
#     reader = csv.reader(f)
#     for origin, destination, duration in reader:
#         db.execute("INSERT INTO flights (origin, destination, duration,) VALUES (:origin, :destination, :duration)",
#                     {"origin":origin, "destination":destination, "duration":duration})
#     db.commit()


if __name__ == "__main__":
    app.run(debug=True)