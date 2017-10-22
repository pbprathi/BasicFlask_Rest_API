from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.employee import Employee,EmployeeList


app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SECRET_KEY']='BHAGEERATH'

jwt=JWT(app,authenticate,identity)

@app.before_first_request
def create_table():
    db.create_all()


api.add_resource(UserRegister,'/register')
api.add_resource(Employee,'/employee/<int:_id>')
api.add_resource(EmployeeList,'/employees')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
