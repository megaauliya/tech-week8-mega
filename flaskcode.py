import pymongo #mengimport library pymongo      
import datetime
from flask import Flask, request 

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://MegaDliyaul20:abcdefgh@cluster0.b7togy4.mongodb.net/?retryWrites=true&w=majority")
db = client['week8']
my_collections = db['mega']
timestamp = datetime.datetime.now()

@app.route('/baksya',methods=['GET','POST'])
def baksya():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    if request.method == 'POST':
    
       results = my_collections.insert_one({"kecepatan":kecepatan,"latitude":latitude,"longitude":longitude, "timestamp":timestamp})
       print(results)
       return {
            "kecepatan":kecepatan,
            "latitude":latitude,
            "longitude":longitude,
            "timestamp":timestamp
                }

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8001, debug = True)
