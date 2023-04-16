from sqlalchemy import create_engine,text
from flask import Flask,jsonify
from flask_restful import Resource, Api, abort, reqparse
import configs as cf

#creating db connection 
engine = create_engine(cf.db_connection('CONNECT_DB_LOCAL'))
conn=engine.connect()

# creating flask app
app = Flask(__name__)
api = Api(app)





class getData(Resource):
    def __init__(self):
        self.sql_query = """select 
        t.id as 'task_id',
        t.task_name as 'task_name',
        s.summary as 'summary'
        from tasks t 
        join task_summary s
        on t.id = s.task_id
        """
    
    def get(self):
        get_data = conn.execute(text(self.sql_query)).fetchall()
        return jsonify(
            id = get_data[0][0],
            task_name = get_data[0][1],
            task_summary = get_data[0][2]
        )



api.add_resource(getData, '/getall')



if __name__ == "__main__":
    app.run()


