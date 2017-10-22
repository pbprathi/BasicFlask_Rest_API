from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.employee import EmployeeModel

class Employee(Resource):

    parse=reqparse.RequestParser()

    parse.add_argument('name',
    type=str,
    required=True,
    help="This field cannot be left blank")

    parse.add_argument('title',
    type=str,
    required=True,
    help="This field cannot be left blank")

    @jwt_required()
    def get(self,_id):
        employee=EmployeeModel.find_by_id(_id)

        if employee:
            return employee.json()
        return {'message':'Employee not found'},404

    def post(self,_id):

        if EmployeeModel.find_by_id(_id):
            return {'message':"Employee with id '{}' already exists.".format(_id)},400

        data=Employee.parse.parse_args()

        employee=EmployeeModel(_id,data['name'],data['title'])

        try:
            employee.save_to_db()
        except:
            return {'message':"An error occured while inserting an employee"},500

        return employee.json(),201

    def put(self,_id):
        data=Employee.parse.parse_args()

        employee=EmployeeModel.find_by_id(_id)
        if employee is None:
            employee=EmployeeModel(_id,data['name'],data['title'])
        else:
            employee.name=data['name']
            employee.title=data['title']
        employee.save_to_db()
        return employee.json()

    def delete(self,_id):
        employee=EmployeeModel.find_by_id(_id)
        if employee:
            employee.delete_from_db()
        return {'message':'successfully deleted the employee'}

class EmployeeList(Resource):
    def get(self):
        return {'Employees':[employee.json() for employee in EmployeeModel.query.all()]}
