# import requests
# import os

# # Get the GitHub token from environment variables
# token = os.getenv('GH_PAT')
# headers = {'Authorization': f'token {token}'}

# def create_issue(repo, title, body):
#     url = f'https://api.github.com/repos/{repo}/issues'
#     data = {'title': title, 'body': body}
#     response = requests.post(url, headers=headers, json=data)
#     return response

# # Example usage
# response = create_issue('ilubimu/KHTC', 'Issue Title', 'Issue Body')
# print(response.json())


import requests
import os
import json

# Get the GitHub token from environment variables
token = os.getenv('GH_PAT')
headers = {'Authorization': f'token {token}'}

# Function to create an issue in the target repository
def create_issue(repo, title, body):
    url = f'https://api.github.com/repos/{repo}/issues'
    data = {'title': title, 'body': body}
    response = requests.post(url, headers=headers, json=data)
    return response

# Get the event payload
with open(os.getenv('GITHUB_EVENT_PATH'), 'r') as event_file:
    event_payload = json.load(event_file)

# Extract the issue title and body from the event payload
issue_title = event_payload['issue']['title']
issue_body = event_payload['issue']['body']

# Example usage
response = create_issue('ilubimu/KHTC', issue_title, issue_body)
print(response.json())

