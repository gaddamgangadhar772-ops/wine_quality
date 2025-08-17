
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
data = joblib.load('model.joblib')
pipe = data['model']
features = data['features']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    values = {}
    if request.method == 'POST':
        vals = []
        for f in features:
            v = request.form.get(f, "").strip()
            values[f] = v
            vals.append(float(v))
        pred = pipe.predict(np.array(vals).reshape(1, -1))[0]
        prediction = round(float(pred), 1)
    return render_template('index.html', features=features, prediction=prediction, values=values)

if __name__ == '__main__':
    app.run(debug=True)
