from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

tasks = { 
    1: {"Task" : "First task", "Summary" : "Summary 1"},
    2: {"Task" : "Second task", "Summary" : "Summary 2"},
}


# adding a request parser to parse post data in json
post_req_parser = reqparse.RequestParser()
post_req_parser.add_argument("Task", type=str, required=True, help="Enter a task name here")
post_req_parser.add_argument("Summary",type=str,required=True,help="Enter a short description for the task")



# creating class to return all todo tasks
class toDos(Resource):
    def get(self):
        return tasks

# creating class to return and add todo task of a particular id
class getTodo(Resource):
    def get(self,todoId):
        return tasks[todoId]

    def post(self, todoId):
        task = post_req_parser.parse_args()
        if todoId in tasks:
            abort(405, "task already exists")
        else:
            tasks[todoId] = {"Task" : task["Task"], "Summary" : task["Summary"]}
        return tasks[todoId]

api.add_resource(toDos,"/todos")
api.add_resource(getTodo,"/todos/<int:todoId>")


if __name__ == '__main__':
    app.run(debug=True)