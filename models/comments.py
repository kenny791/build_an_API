from main import db

class Comment(db.Model):
    # define the table name for the db
    __tablename__= "COMMENTS"

    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    message= db.Column(db.String())
    # two foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('CARDS.id'), nullable=False)

    user = db.relationship ('User', back_populates='comments')
    card = db.relationship ('Card', back_populates='comments')