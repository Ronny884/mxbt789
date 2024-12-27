from app import db
from sqlalchemy.dialects.postgresql import JSONB


class DynamicFormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)
