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

class condo_price_prediction1(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('condo-area', type=str, default='Bang Kapi')
        parser.add_argument('address', type=str, default='ถนนเสรีไทย คลองจั่น บางกะปิ')
        parser.add_argument('year', type=str, default='2011')
        parser.add_argument('sqm', type=int, default= 6470)
        parser.add_argument('tower', type=int, default=2)
        parser.add_argument('floor', type=int, default=30)
        parser.add_argument('price-sqm', type=float, default=52065)
        parser.add_argument('rent-yield', type=float, default=5.81)
        parser.add_argument('rent-yield-inc-year', type=float, default=-23.79)
        parser.add_argument('lat', type=float, default=13.758903)
        parser.add_argument('long', type=float, default=100.649395)
        parser.add_argument('min-dist-station', type=int, default=3757)
        dictp = parser.parse_args()
        condo_area = dictp['condo-area']
        arg2 = dictp['address']
        arg3 = dictp['year']
        arg3 = dictp['sqm']
        arg3 = dictp['tower']
        arg3 = dictp['floor']
        arg3 = dictp['price-sqm']
        arg3 = dictp['rent-yeild']
        arg3 = dictp['rent-yeild-inc-year']
        arg3 = dictp['lat']
        arg3 = dictp['long']
        arg3 = dictp['min-dist-station']
        print(arg1, arg2, arg3)
        res = pcp.get_predict(arg1,arg2,arg3)
        return res

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