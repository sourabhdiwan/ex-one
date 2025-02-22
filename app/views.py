import os
from app import app
from flask import render_template
from app.util import fetch_pipeline_data, fetch_project_data, fetch_jobs_data

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
    project_id = os.getenv('PROJECT_ID')
    pipelines_data = fetch_pipeline_data(project_id)
    return render_template('pipeline.html', pipelines=pipelines_data)

@app.route('/projects')
def projects():
    project_id = os.getenv('PROJECT_ID')
    project_data = fetch_project_data(project_id)
    return render_template('project.html', project=project_data)

@app.route('/jobs/<int:pipeline_id>')
def jobs(pipeline_id):
    project_id = os.getenv('PROJECT_ID')
    jobs_data = fetch_jobs_data(project_id, pipeline_id)
    return render_template('jobs.html', jobs=jobs_data)
