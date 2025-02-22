from flask import current_app
from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

def mydefault(context):
    return context.get_current_parameters()['total_inventory']

class Video(db.Model):
    __tablename__= "video"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime, nullable=True)
    total_inventory = db.Column(db.Integer)
    available_inventory = db.Column(db.Integer, nullable=False, default = mydefault)
    customer = relationship("Rental", back_populates = "video")

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "total_inventory": self.total_inventory,
            "available_inventory": self.get_available_inventory() 
        }

    def is_int(self):
        try:
            return int(self.id)
        except ValueError:
            return False

    def get_available_inventory(self):
        return self.total_inventory - len(self.customer)
