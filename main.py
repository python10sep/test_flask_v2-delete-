"""

#################################################################
NOTES

## project structure

test_flask_v2 (project root)

    - main.py
    - static (directory)
    - templates (package)
        -- __init__.py
        -- welcome.html
    - models (package)
        - __init__.py
        - dal.py
        - flashcard_db.json
    - requirements.txt


#################################################################
"""


from flask import Flask, render_template, abort
from models.dal import db


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index)
    except IndexError:
        abort(404)



