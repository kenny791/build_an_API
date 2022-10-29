from main import ma
from marshmallow import fields
from marshmallow.validate import Length, OneOf, Regexp, And

VALID_PRIORITIES = ('Urgent', 'High', 'Low', 'Medium')
VALID_STATUSES = ('To Do', 'Done', 'Ongoing', 'Testing', 'Deployed')

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CardSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=("email",))
    comments = fields.List(fields.Nested("CommentSchema"))
    title = fields.String(required=True, validate=And(Length(min=1), Regexp('^[a-zA-Z0-9 ]+$')))    
    status = fields.String(required=True, validate=OneOf(VALID_STATUSES))
    priority = fields.String(load_default='Medium', validate=OneOf(VALID_PRIORITIES))        
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority", "user", "comments")

#single card schema, when one card needs to be retrieved
card_schema = CardSchema()
#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)