from app import db

class Words(db.Model):
    __tablename__="Words"
    id = db.Column(db.Integer, primary_key=True) 
    word = db.Column(db.String(12))
    part = db.Column(db.Enum('verb', 'noun', 'adverb', 'adjective'))
