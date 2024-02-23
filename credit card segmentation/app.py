from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
data = pd.read_csv('c:\Users\Sarvu\Desktop\UG PHASE-1\CC GENERAL.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segment', methods=['POST'])
def segment():
    # Get data from the form
    data = request.form['data']

    # Process data (perform clustering)
    # Here you'll use your clustering algorithm
    # This is just a placeholder
    processed_data = process_data(data)

    return render_template('segment.html', result=processed_data)

def process_data(data):
    # Dummy function for data processing
    return data

if __name__ == '__main__':
    app.run(debug=True)

