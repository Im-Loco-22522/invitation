import sys
from flask import Flask, render_template

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"
FLATPAGES_ROOT = "content"

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template("index.html", bigheader=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
