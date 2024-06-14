# import requests
# import os
# import json

# # Get the GitHub token from environment variables
# token = os.getenv('GH_PAT')
# headers = {'Authorization': f'token {token}'}

# # Function to create an issue in the target repository
# def create_issue(repo, title, body):
#     url = f'https://api.github.com/repos/{repo}/issues'
#     data = {'title': title, 'body': body}
#     response = requests.post(url, headers=headers, json=data)
#     return response

# # Get the event payload
# with open(os.getenv('GITHUB_EVENT_PATH'), 'r') as event_file:
#     event_payload = json.load(event_file)

# # Extract the issue title and body from the event payload
# issue_title = event_payload['issue']['title']
# issue_body = event_payload['issue']['body']

# # Example usage
# response = create_issue('ilubimu/KHTC', issue_title, issue_body)
# print(response.json())

import requests
import os
import json

# Get the GitHub token from environment variables
token = os.getenv('GH_PAT')
headers = {'Authorization': f'token {token}'}

# Function to create or update an issue in the target repository
def sync_issue(repo, issue_data):
    # Check if the issue already exists in the target repo
    existing_issue = find_existing_issue(repo, issue_data['title'])
    
    # If it does, update it
    if existing_issue:
        update_issue(repo, existing_issue['number'], issue_data)
    # Otherwise, create a new one
    else:
        create_issue(repo, issue_data)

# Function to find an existing issue by title
def find_existing_issue(repo, title):
    url = f'https://api.github.com/repos/{repo}/issues'
    response = requests.get(url, headers=headers)
    issues = response.json()
    for issue in issues:
        if issue['title'] == title:
            return issue
    return None

# Function to update an existing issue
def update_issue(repo, issue_number, issue_data):
    url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
    response = requests.patch(url, headers=headers, json=issue_data)
    return response

# Function to create a new issue
def create_issue(repo, issue_data):
    url = f'https://api.github.com/repos/{repo}/issues'
    response = requests.post(url, headers=headers, json=issue_data)
    return response

# Get the event payload
with open(os.getenv('GITHUB_EVENT_PATH'), 'r') as event_file:
    event_payload = json.load(event_file)

# Extract the issue title and body from the event payload
issue_title = event_payload['issue']['title']
issue_body = event_payload['issue']['body']

# Example usage
issue_data = {'title': issue_title, 'body': issue_body}
response = sync_issue('ilubimu/testtrace', issue_data)
print(response.json())
