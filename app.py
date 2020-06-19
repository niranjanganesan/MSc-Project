from flask import Flask, request, jsonify, render_template
import json
import geojson
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    with open('points.geojson') as f:
        data = json.load(f)
    coords = []
    for feature in data['features']:
        coord0 = feature['geometry']['coordinates'][0]
        coord1 = feature['geometry']['coordinates'][1]
        cd = 'new google.maps.LatLng' + str('(') + str(coord1) + str(',') + str(coord0) + str(')')
        coords.append(cd)
    aa = map(str, coords)
    abc = ",".join(aa)
    print(abc[0])
    return render_template("index.html", coord = abc)
if __name__ == "__main__":
    app.run(debug = True)
