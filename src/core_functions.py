import os
from urllib.parse import urlparse

def delete_file_content():
    with open('code.txt', 'w') as file:
        file.write('')
        file.close()

def save_code_in_file(code):
    with open('code.txt', 'a') as file:
        file.write(code)
        file.close()

def extract_repo_owner(repo_url):
    parsed_url = urlparse(repo_url)
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.strip('/').split('/')

        if len(path_parts) >= 2:
            owner = path_parts[0]
            return owner
        else:
            raise ValueError("Invalid GitHub URL format")
    else:
        raise ValueError("Not a valid GitHub URL")

def extract_repo_name(repo_url):
    parsed_url = urlparse(repo_url)
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.strip('/').split('/')
        if len(path_parts) >= 2:
            repo_name = path_parts[1]
            return repo_name
        else:
            raise ValueError("Invalid GitHub URL format")
    else:
        raise ValueError("Not a valid GitHub URL")

def extract_repo_branch(repo_url):
    parsed_url = urlparse(repo_url)
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.strip('/').split('/')
        if len(path_parts) >= 2:
            repo_branch = path_parts[3]
            return repo_branch
        else:
            raise ValueError("Invalid GitHub URL format")
    else:
        raise ValueError("Not a valid GitHub URL")

