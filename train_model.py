
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv('data/winequality-red.csv', sep=';')

X = df.drop('quality', axis=1)
y = df['quality']

# Pipeline with scaling + model
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(n_estimators=400, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe.fit(X_train, y_train)
preds = pipe.predict(X_test)

print(f"R^2: {r2_score(y_test, preds):.3f}")
print(f"MAE: {mean_absolute_error(y_test, preds):.3f}")

joblib.dump({'model': pipe, 'features': list(X.columns)}, 'model.joblib')
print("Saved model.joblib")
