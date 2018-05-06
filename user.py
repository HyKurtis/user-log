class User:

    def __init__(self, name):
        self.name = name
        self.info = {
            "age": "Unknown",
            "job": "Unknown",
            "country": "Unknown"
        }

    def set_value(self, key, value):
        key = str.lower(key)

        if key in self.info:
            self.info[key] = value
            return True
        else:
            return False

    def get_value(self, key):
        key = str.lower(key)

        if key in self.info:
            return self.info[key]
        else:
            return None

    def key_exists(self, key):
        key = str.lower(key)
        return key in self.info