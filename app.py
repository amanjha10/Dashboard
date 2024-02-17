from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("pothole-detection-e0430-firebase-adminsdk-w5s08-09986225f7.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pothole-detection-e0430-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# ref = db.reference('Potholes')
# data = ref.get()
# print(data)

# @app.route('/')
# def render_data():
#     ref = db.reference('Fire')
#     data = ref.get()
#     print(data)
#     return render_template('index.html', data=data)
# @app.route('/')
# def render_data():
#     ref = db.reference('Fire')
#     data = ref.get()
#     if data:
#         data_list = [{'name':v['name'], 'contact':v['phone-number'],'lat': v['lat'], 'lng': v['lng'], 'time': v['time'],} for k, v in data.items()]
#     else:
#         data_list = []
#     ref = db.reference('Potholes')
#     data = ref.get()
#     if data:
#         dataa_list = [{'lat': v['lat'], 'lng': v['lng'],} for k, v in data.items()]
#     else:
#         dataa_list = []
    
#     return render_template('index.html', data=[data_list,dataa_list])

@app.route('/')
def renderr_data():
    ref = db.reference('Potholes')
    data = ref.get()
    print(data)
    if data:
        data_list = [{'lat': v['lat'], 'lng': v['lng'],} for k, v in data.items()]
    else:
        data_list = []
    return render_template('index.html', dataa=data_list)

if __name__ == '__main__':
    app.run(debug=True)
# your-database-name.firebaseio.com