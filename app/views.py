import os
from app import app
from flask import render_template
from app.utils import fetch_gitlab_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/pipelines')
def pipelines():
    gitlab_token = os.getenv('GITLAB_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    headers = {"Authorization": f"Bearer {gitlab_token}"}
    
    pipelines_endpoint = f"projects/{project_id}/pipelines"
    pipelines_data = fetch_gitlab_data(pipelines_endpoint, headers)
    
    return render_template('pipeline.html', pipelines=pipelines_data)
