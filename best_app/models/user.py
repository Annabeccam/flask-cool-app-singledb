# encoding: utf-8


from best_app.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True, nullable=False)    
    created_at = db.Column(db.Date, nullable=False)
    role = db.Column(db.String(), default="employee")    


    __table_args__ = (
        db.CheckConstraint(role.in_(['student', 'teacher', 'employee']), name='role_types'),      
    )