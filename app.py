from flask import Flask, request,jsonify,render_template
import util

app=Flask(__name__)

util.load_data()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_location_name')
def get_location_name():
    response=jsonify({
        'locations':util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/get_price',methods=['POST'])
def get_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response=jsonify({
        'estimated_price':util.get_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__=="__main__":
    app.run()