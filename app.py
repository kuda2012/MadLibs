from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def mad_libs_form():
    return render_template("form.html")

@app.route("/story")
def create_story():
    place = request.args["place"]
    verb = request.args["verb"]
    noun = request.args["noun"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("story.html", place=place, verb=verb, noun=noun,
    adjective = adjective, plural_noun = plural_noun)