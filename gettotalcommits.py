import requests

def get_total_commits(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?per_page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        link_header = response.headers.get('Link', None)
        if link_header:
            # Extract the last page number from the Link header
            last_page_url = link_header.split(',')[-1].split(';')[0].strip('<>')
            last_page = int(last_page_url.split('=')[-1])
            print(f"Total number of commits pages: {last_page}")
            return last_page
        else:
            # Only one page of commits
            return 1
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return None

repo_owner = "torvalds"
repo_name = "linux"
total_pages = get_total_commits(repo_owner, repo_name)
