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

import json
from flask import Flask, render_template, abort, jsonify, request, Response
from models.dal import db, save_to_db


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html", cards=db)


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template(
            "card.html",
            card=card,
            index=index
        )
    except IndexError:
        abort(404)


@app.route("/add", methods=["POST"])
def add_card():
    data = request.get_json()
    # validation on request data

    db.append(data)
    save_to_db(db)

    obj = json.dumps({"success": 201})

    # data validation before response
    return Response(obj, status=201, mimetype="application/json")


@app.route("/api/cards")
def api_card_list():
    return jsonify(db)
