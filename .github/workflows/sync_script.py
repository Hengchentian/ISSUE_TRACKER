import requests
import os

# Get the GitHub token from environment variables
token = os.getenv('GH_PAT')
headers = {'Authorization': f'token {token}'}

def create_issue(repo, title, body):
    url = f'https://api.github.com/repos/{repo}/issues'
    data = {'title': title, 'body': body}
    response = requests.post(url, headers=headers, json=data)
    return response

# Example usage
response = create_issue('ilubimu/KHTC', 'Issue Title', 'Issue Body')
print(response.json())
