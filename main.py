from flask import Flask
from classes.return_result import Result
import json


def json_d():
    with open("candidates.json", "r", encoding="utf-8") as f:
        text_json = json.load(f)
    return text_json


app = Flask(__name__)
json = Result(json_d())


@app.route("/")
def page_index():
    return json.home_page()


@app.route("/candidate/<can>/")
def page_profile(can):
    return json.candidate(can)


@app.route("/skill/<cand_skills>/")
def page_feed(cand_skills):
    return json.skills(cand_skills)


if __name__ == "__main__":
    app.run()




