from flask import Flask, render_template, request
from sklearn.cluster import KMeans
import pandas as pd

app = Flask(__name__)

# Load sample data
data = pd.read_csv('c:\Users\Sarvu\Desktop\UG PHASE-1\CC GENERAL.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segment', methods=['POST'])
def segment():
    num_clusters = int(request.form['num_clusters'])
    
    # Perform clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(data[['AnnualIncome', 'SpendingScore']])
    
    # Add cluster labels to the dataset
    data['Cluster'] = kmeans.labels_
    
    # Prepare data for visualization
    clustered_data = []
    for cluster_id in range(num_clusters):
        clustered_data.append(data[data['Cluster'] == cluster_id][['AnnualIncome', 'SpendingScore']].values.tolist())
    
    return render_template('index.html', clustered_data=clustered_data)

if __name__ == '__main__':
    app.run(debug=True)
