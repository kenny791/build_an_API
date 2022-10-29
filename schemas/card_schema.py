from main import ma
from marshmallow import fields,validates
from marshmallow.validate import Length, OneOf, Regexp, And
from marshmallow.exceptions import ValidationError
from models.cards import Card

VALID_PRIORITIES = ('Urgent', 'High', 'Low', 'Medium')
VALID_STATUSES = ('To Do', 'Done', 'Ongoing', 'Testing', 'Deployed')

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CardSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=("email",))
    comments = fields.List(fields.Nested("CommentSchema"))
    title = fields.String(required=True, validate=And(Length(min=1), Regexp('^[a-zA-Z0-9 ]+$')))    
    status = fields.String(required=True, validate=OneOf(VALID_STATUSES))
    priority = fields.String(load_default='Medium', validate=OneOf(VALID_PRIORITIES))        

    @validates('status')
    def validate_status(self, value):
        # Only apply this validator if the attempted status is 'Ongoing'
        if value == 'Ongoing':
            # Get a count of cards that already have the 'Ongoing' status
            count = Card.query.filter_by(status='Ongoing').count()
            if count > 1:
                raise ValidationError('You already have an ongoing card')

    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority", "user", "comments")

#single card schema, when one card needs to be retrieved
card_schema = CardSchema()
#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)