from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class helloWorld(Resource):
    def get(self):
        return {"data": "Hello world"}

class helloName(Resource):
    def get(self,name):
        return {"data": f"Hello {name}"}



api.add_resource(helloWorld,'/helloworld')
api.add_resource(helloName,'/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)