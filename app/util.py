import os
import requests

def fetch_gitlab_data(endpoint):
    gitlab_token = os.getenv('GITLAB_TOKEN')
    headers = {"Authorization": f"Bearer {gitlab_token}"}
    url = f"https://gitlab.com/api/v4/{endpoint}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to fetch pipeline data
def fetch_pipeline_data(project_id):
    endpoint = f"projects/{project_id}/pipelines"
    return fetch_gitlab_data(endpoint)

# Function to fetch project data
def fetch_project_data(project_id):
    endpoint = f"projects/{project_id}"
    return fetch_gitlab_data(endpoint)

# Function to fetch jobs for a pipeline
def fetch_jobs_data(project_id, pipeline_id):
    endpoint = f"projects/{project_id}/pipelines/{pipeline_id}/jobs"
    return fetch_gitlab_data(endpoint)

# Function to fetch individual pipeline data
def fetch_individual_pipeline_data(project_id, pipeline_id):
    endpoint = f"projects/{project_id}/pipelines/{pipeline_id}"
    return fetch_gitlab_data(endpoint)
