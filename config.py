# Replace 'repo_owner' and 'repo_name' with the desired repository's owner and name
repo_owner="torvalds"
repo_name="linux"
token=None  # Add your GitHub token here if needed

# GitHub API Rate Limits:
# Unauthenticated Requests: You are limited to 60 requests per hour per IP address.
# Authenticated Requests: With a personal access token, you can make up to 5,000 requests per hour.
per_page=100 
requests_per_hour=50
