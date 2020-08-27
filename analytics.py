import json

class Analytics:
    def __init__(self):
        pass;

    def echo(self, json_in):
        data = json.loads(json_in)
        data['Solution Provider'] = "Dave ID"
        return json.dumps(data)
