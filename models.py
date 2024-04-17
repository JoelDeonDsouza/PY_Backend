from config import db


# Model data user //
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    # json formatted render //
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
