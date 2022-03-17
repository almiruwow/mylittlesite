class Result:
    def __init__(self, json_data):
        self.json_data = json_data

    def home_page(self):
        str_ = ''
        for dict_ in self.json_data:
            str_ += dict_['name'] + '\n' + str(dict_['id']) + '\n' + dict_['skills'] + '\n' + '\n'
        return f"<pre>{str_}</pre>"

    def candidate(self, can):
        return_candidate = self.json_data[int(can) - 1]
        return f'<img src={return_candidate["picture"]}>' + f'<pre>{return_candidate["name"]}\n{return_candidate["id"]}\n{return_candidate["skills"]}</pre>'

    def skills(self, cand_skills):
        str_ = ''
        for dict_ in self.json_data:
            new_dict = dict_["skills"].lower().split(', ')
            if cand_skills in new_dict:
                str_ += dict_['name'] + '\n' + str(dict_['id']) + '\n' + dict_['skills'] + '\n' + '\n'
        return f"<pre>{str_}</pre>"
