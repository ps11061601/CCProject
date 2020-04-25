from flask import Flask, request, render_template
from flask.logging import create_logger
import logging

import joblib

# Import from Python Scripts
from model import InputForm
from my_functions import create_dataframe
import numpy

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


# App Pages

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/About')
def about():
    return render_template("about.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    form = InputForm(request.form)
    print(form)
    LOG.info("Form Require: {form}")

    if request.method == 'POST' and form.validate():
        # Convert Input Table Data to DataFrame
        clf = joblib.load('ny_airbnb_prediction.joblib')
        df_input = create_dataframe(form)
        LOG.info("Convert Input to DataFrame: {df_input}")
        # Predict Price
        prediction = clf.predict(df_input)
        LOG.info("Predict: {prediction}")
        # Convert to String Output
        final_output = "Predicted Price: $" + str(numpy.power(10, prediction))[1:-1]
        result = final_output
        print("output")
        print(final_output)

    else:
        result = None

    return render_template('predict.html', form=form, result=result)



# @app.route("/predict", methods=['POST'])
# def predict():
#     """Performs an sklearn prediction
#     input looks like:
#             {"neighbourhood_group":{"22835":3},"neighbourhood":{"22835":104},"room_type":{"22835":0},"number_of_reviews":{"22835":43},"reviews_per_month":{"22835":1.68},"availability_365":{"22835":252}}
#     result looks like:
#     { "prediction": [ 20.35373177134412 ] }
#     """


#     json_payload = request.json
#     LOG.info(f"JSON payload: {json_payload}")
#     inference_payload = pd.DataFrame(json_payload)
#     LOG.info(f"inference payload DataFrame: {inference_payload}")
#     scaled_payload = scale(inference_payload)
#     prediction = list(clf.predict(scaled_payload))
#     return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
