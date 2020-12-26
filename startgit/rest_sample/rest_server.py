from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse

#Flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)

# get 정의


class class_restapi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data')
        args = parser.parse_args()
        receive_data = args["data"]
        print(receive_data)
        receive_data += " world rest_api"
        return receive_data


api.add_resource(class_restapi, '/sample_restapi')

#서버 실행
if __name__ == '__main__':
    app.run()
