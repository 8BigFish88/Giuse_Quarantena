from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    ricette = db.relationship('Ricetta', backref='author', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Ricetta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(64), index=True, unique=True)
    ingredienti = db.Column(db.String(255))
    procedimento = db.Column(db.String(255))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
