# ex-one

## Overview
The **ex-one** dashboard is a web-based application built using Python and Flask. It provides a comprehensive view of test execution cycles, leveraging data from the GitLab API and storing it in a PostgreSQL database. The dashboard includes features like current cycle status, historical data analysis, and API configuration settings.

## Features
1. **Current Cycle Status:**
   - Visual representation of the test execution cycle status using charts.
   - Key metrics including tests executed, passed, failed, and pending.

2. **Historical Data:**
   - Detailed view of historical test execution data with filters.
   - Option to export historical data to CSV for further analysis.

3. **API Integration:**
   - Configuration options for GitLab API integration.
   - Scheduled tasks for periodic data synchronization with GitLab.

## Architecture
- **Frontend:** HTML, CSS, JavaScript, Flask templates
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **API Integration:** Python scripts for fetching data from GitLab API
- **Scheduled Tasks:** Celery (or any other task scheduler) for periodic updates

### Data Flow
1. GitLab API -> Python Script -> PostgreSQL Database -> Flask Backend -> Frontend

## Setup and Installation
### Prerequisites
- Python 3.x
- PostgreSQL
- GitLab account and access token

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ex-one.git
   cd ex-one

Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
pip install -r requirements.txt
Set up PostgreSQL database:

Create a new database for the project.

Update the config.py file with your database credentials.

Configure GitLab API:

Update the config.py file with your GitLab API credentials and endpoint.

Initialize the database:

bash
flask db init
flask db migrate
flask db upgrade
Run the application:

bash
flask run
Usage
Access the dashboard at http://127.0.0.1:5000/.

Navigate through the different views: Dashboard, Historical Data, and API Configurations.

Configure the GitLab API settings and initiate data synchronization.

Contributing
Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature-branch)

Open a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the open-source community for the tools and libraries used in this project.

Special thanks to the contributors for their valuable input and feedback.