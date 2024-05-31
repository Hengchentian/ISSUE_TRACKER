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

# Get the GitHub token and event path from environment variables
token = os.getenv('GH_PAT')
event_path = os.getenv('GITHUB_EVENT_PATH')
headers = {'Authorization': f'token {token}'}

# Function to create or update an issue in the target repository
def sync_issue(repo, issue_data):
    # Check if the issue already exists in the target repo
    # If it does, update it; otherwise, create a new one
    # ...

# Function to add a comment to an existing issue in the target repository
def add_comment(repo, issue_number, comment_body):
    url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/comments'
    data = {'body': comment_body}
    response = requests.post(url, headers=headers, json=data)
    return response

# Read the event payload
with open(event_path, 'r') as event_file:
    event_payload = json.load(event_file)

# Determine the type of event and act accordingly
if 'issue' in event_payload:
    # Sync issue details
    issue_data = {
        'title': event_payload['issue']['title'],
        'body': event_payload['issue']['body']
    }
    sync_issue('ilubimu/KHTC', issue_data)
elif 'comment' in event_payload:
    # Sync issue comment
    comment_body = event_payload['comment']['body']
    issue_number = event_payload['issue']['number']  # You'll need to map this to the corresponding issue in the target repo
    add_comment('ilubimu/KHTC', issue_number, comment_body)

# Example usage
response = sync_issue('ilubimu/KHTC', issue_data)
print(response.json())
