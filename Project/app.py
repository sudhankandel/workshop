
from flask import Flask,render_template, request
from load_model import model_operation


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def index():
    if request.method=='POST':
        income=request.form['Income']
        house_age=request.form['House_age']
        number_of_rooms=request.form['Number_of_rooms']
        number_of_bedrooms=request.form["Number_of_bedrooms"]
        population=request.form['Population']
        prediction=model_operation(income,house_age,number_of_rooms,number_of_bedrooms,population)
        data={'income':income,
            'prediction':prediction}
        return render_template('index.html',data=data,)
    else:
        return render_template('index.html',data=[])

if __name__ == "__main__":
    app.run(debug=True)