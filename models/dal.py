"""
DAL : Data Access Layer

This module contains code to retrieve and store data (data manipulation)
"""

import json
from typing import Dict


def load_db() -> Dict:
    """load data from json file into python object"""

    file_path = "/Users/prashant/PICT/VELOCITY 10Sep/test_flask_v2/models/flashcard_db.json"
    with open(file_path, "r") as foo:
        return json.load(foo)


def save_to_db(db_):
    file_path = "/Users/prashant/PICT/VELOCITY 10Sep/test_flask_v2/models/flashcard_db.json"

    # with operator closes file automatically
    # with operator is `context-manager`
    with open(file_path, "w") as fp:
        json.dump(db_, fp)


db = load_db()
