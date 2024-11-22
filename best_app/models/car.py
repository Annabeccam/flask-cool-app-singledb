# encoding: utf-8


from best_app.database import db
from sqlalchemy import ForeignKeyConstraint
from best_app.models.user import User 


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)     
    model = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)    

    
    __table_args__ = (        
        ForeignKeyConstraint([owner_id], [User.id], ondelete='NO ACTION'),        
    )