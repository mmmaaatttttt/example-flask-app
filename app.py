from flask import Flask, render_template, request

app = Flask(__name__)

cool_colors = [
    "cornsilk",
    "firebrick",
    "peachpuff"
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/colors", methods=["POST"])
def new_color():
    color = request.json['color']
    return { "color": color, "isCool": color.lower() in cool_colors }


@app.route("/cool_colors")
def all_cool_colors():
    return { "cool_colors": cool_colors }
