import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def fetch_gitlab_data(endpoint):
    gitlab_token = os.getenv('GITLAB_TOKEN')
    headers = {"Authorization": f"Bearer {gitlab_token}"}
    url = f"https://gitlab.com/api/v4/{endpoint}"
    
    # Create a session
    session = requests.Session()
    
    # Define a retry strategy
    retry_strategy = Retry(
        total=3,  # Number of retries
        status_forcelist=[429, 500, 502, 503, 504],  # Retry on these status codes
        allowed_methods=["HEAD", "GET", "OPTIONS"],  # Retry on these methods
        backoff_factor=1  # Wait time between retries
    )
    
    # Mount the retry strategy to the session
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    # Make the request
    response = session.get(url, headers=headers)
    
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
