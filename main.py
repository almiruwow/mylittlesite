from flask import Flask
import json

with open("candidates.json", "r") as f:
    text_json = json.load(f)

app = Flask(__name__)


@app.route("/")
def page_index():
    str_ = ''
    for dict_ in text_json:
        str_ += dict_['name'] + '\n' + str(dict_['id']) + '\n' + dict_['skills'] + '\n' + '\n'
    return f"<pre>{str_}</pre>"


@app.route("/candidate/<can>/")
def page_profile(can):
    return_candidate = text_json[int(can) - 1]
    return f'<img src={return_candidate["picture"]}>' + f'<pre>{return_candidate["name"]}\n{return_candidate["id"]}\n{return_candidate["skills"]}</pre>'


@app.route("/skill/<cand_skills>/")
def page_feed(cand_skills):
    str_ = ''
    for dict_ in text_json:
        new_dict = dict_["skills"].lower().split(', ')
        if cand_skills in new_dict:
            str_ += dict_['name'] + '\n' + str(dict_['id']) + '\n' + dict_['skills'] + '\n' + '\n'
    return f"<pre>{str_}</pre>"

app.run(host='0.0.0.0', port=8000)
