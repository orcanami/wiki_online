import json
with open("user_data.json") as fin:
    data = json.load(fin)
usernames['wikipedia']['en'] = data["username"]
authenticate['*.wikipedia.org'] = (data["username"],data["password"])
