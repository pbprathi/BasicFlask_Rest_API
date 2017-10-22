from db import db

class EmployeeModel(db.Model):

    __tablename__='employee'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    title=db.Column(db.String(100))

    def __init__(self,_id,name,title):
        self.id=_id
        self.name=name
        self.title=title

    def json(self):
        return {'id':self.id,'name':self.name,'title':self.title}

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
