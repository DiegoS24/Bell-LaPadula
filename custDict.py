class cust_dict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value