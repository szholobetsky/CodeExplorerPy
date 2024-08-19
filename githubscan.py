#!/usr/bin/env python3
#
#  githubscan.py
#  
#  Copyright 2024 Stanislav Zholobetskyi 
#    
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys
import requests
import time
import config


# Function to fetch and display commit details
def get_github_commits(repo_owner, repo_name, token=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

def get_github_commits(repo_owner, repo_name, token=None, per_page=100, requests_per_hour=50):
    page = 1
    delay = 3600 / requests_per_hour  # Calculate delay between requests

    while True:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?per_page={per_page}&page={page}"
        headers = {}
    
        if token:
            headers['Authorization'] = f'token {token}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            if not commits:
                break  # Exit loop if there are no more commits
            for commit in commits:
                commit_sha = commit['sha']
                commit_message = commit['commit']['message']
                commit_author = commit['commit']['author']['name']
                commit_url = commit['url']

                commit_details = requests.get(commit_url).json()
                files_changed = [file['filename'] for file in commit_details.get('files', [])]

                print(f"Commit SHA: {commit_sha}")
                print(f"Author: {commit_author}")
                print(f"Message: {commit_message}")
                print(f"Files Changed: {', '.join(files_changed)}")
                print("-" * 40)

            page += 1  # Move to the next page

            # Sleep to control the rate of requests
            time.sleep(delay)
        else:
            print(f"Failed to fetch commits: {response.status_code}")
            break




def main(args):
    get_github_commits(config.repo_owner, config.repo_name, config.token, config.per_page, config.requests_per_hour)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
