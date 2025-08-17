
# 🍷 Wine Quality Prediction Website

![image alt](https://github.com/gaddamgangadhar772-ops/wine_quality/blob/689b10b00c4f5ee26377b6c001859eef23cafed4/wine_quality%20output.png)

Two ways to run:
- **Streamlit app** (`app_streamlit.py`) — quickest way to get a website.
- **Flask app** (`app_flask.py` + `templates/index.html`) — classic website stack.

## 1) Setup (Windows / macOS / Linux)

```bash
# 1) Create & activate a virtual environment (recommended)
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
```

## 2) Get the dataset
This project uses the **UCI Red Wine Quality** dataset.

```bash
# Download via script (recommended)
python get_data.py
# -> downloads to data/winequality-red.csv
```

If the script fails due to lack of internet, you can manually place the CSV at: `data/winequality-red.csv`.

## 3) Train the model

```bash
python train_model.py
```
This will create: `model.joblib`

## 4A) Run the Streamlit website (quick)
```bash
streamlit run app_streamlit.py
```
Look for the local URL in the terminal (usually http://localhost:8501).

## 4B) Run the Flask website (classic)
```bash
# Development server
python app_flask.py
# Visit http://127.0.0.1:5000
```

## 5) Deploy options
- **Streamlit Community Cloud**: Push this folder to GitHub and deploy `app_streamlit.py`.
- **Render (Flask)**: Uses the included `Procfile` with `gunicorn`.

See the main Chat message for step-by-step deployment links.

## Project tree
```
wine-quality-site/
├─ data/
│  └─ winequality-red.csv        # created by get_data.py
├─ templates/
│  └─ index.html                 # Flask UI
├─ app_streamlit.py              # Streamlit site
├─ app_flask.py                  # Flask site
├─ get_data.py                   # downloads dataset
├─ train_model.py                # trains and saves model.joblib
├─ requirements.txt
├─ Procfile                      # for Render (Flask)
└─ README.md
```
