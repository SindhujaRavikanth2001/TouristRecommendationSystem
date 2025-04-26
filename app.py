from flask import Flask, render_template, request
from Main import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    id = '213'
    feature_cols = ['userid', 'dance_clubs', 'restaurants', 'museums', 'resorts', 'theaters', 'religious_institutions',
                    'location']
    #art_galleries = request.form['art_galleries']
    dance_clubs = request.form['dance_clubs']
    #juice_bars = request.form['juice_bars']
    restaurants = request.form['restaurants']
    museums = request.form['museums']
    resorts = request.form['resorts']
    #parks_picnic_spots = request.form['parks_picnic_spots']
    #beaches = request.form['beaches']
    theaters = request.form['theaters']
    religious_institutions = request.form['religious_institutions']
    os.remove("file.txt")
    with open('file.txt', "a") as f:
        f.write('userid,dance_clubs,restaurants,museums,resorts,theaters,religious_institutions\n')
        f.write(id+',')
        #f.write(art_galleries+',')
        f.write(dance_clubs+',')
        #f.write(juice_bars+',')
        f.write(restaurants+',')
        f.write(museums+',')
        f.write(resorts+',')
        #f.write(parks_picnic_spots+',')
        #f.write(beaches+',')
        f.write(theaters+',')
        f.write(religious_institutions)
    upload()
    featureSelection()
    decisionTree()
    return predict()
    #return output()

if __name__ == '__main__':
    app.run(debug=True)
