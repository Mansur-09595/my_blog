from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def about():
    return render_template("about.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/index", methods=["GET","POST"])
def index():
    if session.get('notes') is None:
        session['notes'] = []
    if request.method == "POST":
        note = request.form.get("note")
        session['notes'].append(note)   

    return render_template("index.html", notes=session['notes'])

@app.route("/hello", methods=["POST"])
def hello():
    take = request.form.get("name")
    text = take
    with open('text.txt', 'w', encoding="utf-8") as txt_file:
        txt_file.write(text)
    return render_template("hello.html", message=take)


if __name__ == "__main__":
    app.run(debug=True)