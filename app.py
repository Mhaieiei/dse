# app.py
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api, reqparse
import predict_condo_price as pcp
app = Flask(__name__)
api = Api(app)

# A welcome message to test our server
@app.route('/')
def index():
    return render_template("index.html")

class condo_price_prediction(Resource):
    def post(self):
        print('test call')
        data = request.get_json()
        res = pcp.get_predict(data)
        return res

api.add_resource(condo_price_prediction, '/condo-price-predict',endpoint='condo-price-predict')
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)