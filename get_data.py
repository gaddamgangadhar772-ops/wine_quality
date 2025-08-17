
import os
import urllib.request

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
DEST = os.path.join("data", "winequality-red.csv")

os.makedirs("data", exist_ok=True)
print("Downloading dataset...")
urllib.request.urlretrieve(URL, DEST)
print(f"Done: {DEST}")
