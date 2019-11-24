from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from joblib import load
import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def predict():
    # Get the data
    data = request.get_json(force=True)

    if (data['body'] == []): # empty list
        return jsonify(
            error_code=400,
            message="body must not be an empty list"
        )
    else:
        # Get the data
        df = pd.DataFrame(data['body'])

        # Load the model
        clf_rf = load(r'/home/crowsad/mysite/model.pkl')

        # Generate prediction
        pred = clf_rf.predict(df)

        return jsonify(
            data=df.to_dict(orient='records'),
            pred=str(pred[0])
        )

@app.route('/prediction', methods=['GET'])
@cross_origin()
def predict_ui():
    # Get the query string, this endpoint only serves single data
    feat1 = request.args.get('feature1')
    feat2 = request.args.get('feature2')
    feat3 = request.args.get('feature3')
    feat4 = request.args.get('feature4')
    feat5 = request.args.get('feature5')
    feat6 = request.args.get('feature6')
    feat7 = request.args.get('feature7')	

    # Get the data
    X = [
            {
                "att1": float(feat1),
                "att2": float(feat2),
                "att3": float(feat3),
                "att4": float(feat4),
                "att5": float(feat5),
                "att6": float(feat6),
                "att7": float(feat7)
            }
        ]
    df = pd.DataFrame(X)

    # Load the model
    clf_rf = load(r'/home/crowsad/mysite/model.pkl')

    # Generate prediction
    pred = clf_rf.predict(df)

    return jsonify(
        data=df.to_dict(orient='records'),
        pred=str(pred[0])
    )