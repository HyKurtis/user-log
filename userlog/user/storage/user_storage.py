from userlog.user.user import User
import json
import io


class UserStorage:

    def export_to(self, users, location):
        data = []

        for user in users:
            data.append(self.to_json(user))

        with io.open(location, 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=True, indent=4)

    def import_from(self, location):
        users = []

        with io.open(location) as data_file:
            data = json.load(data_file)

            for section in data:
                user = self.from_json(section)
                users.append(user)

        return users

    def to_json(self, user):
        return {"name": user.name, "info": user.info}

    def from_json(self, data):
        name = data["name"]
        info = data["info"]

        user = User(name)

        for key in info:
            value = info[key]
            user.set_value(key, value)

        return user
