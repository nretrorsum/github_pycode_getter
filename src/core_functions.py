import os
from urllib.parse import urlparse

def delete_file_content():
    with open('../code.txt', 'w') as file:
        file.write('')
        file.close()

def save_code_in_file(code):
    with open('../code.txt', 'a') as file:
        file.write(code)
        file.close()

def extract_repo_owner(repo_url):
    # Парсинг URL для витягування частин
    parsed_url = urlparse(repo_url)

    # Перевірка, що URL правильний і має правильний формат
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.strip('/').split('/')

        # Перевірка на правильну кількість частин (власник/репозиторій)
        if len(path_parts) >= 2:
            owner = path_parts[0]
            return owner
        else:
            raise ValueError("Invalid GitHub URL format")
    else:
        raise ValueError("Not a valid GitHub URL")

def extract_repo_name(repo_url):
    # Парсинг URL для витягування частин
    parsed_url = urlparse(repo_url)

    # Перевірка, що URL правильний і має правильний формат
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.strip('/').split('/')

        # Перевірка на правильну кількість частин (власник/репозиторій)
        if len(path_parts) >= 2:
            repo_name = path_parts[1]
            return repo_name
        else:
            raise ValueError("Invalid GitHub URL format")
    else:
        raise ValueError("Not a valid GitHub URL")

def extract_repo_branch(repo_url):
    # Парсинг URL для витягування частин
    parsed_url = urlparse(repo_url)

    # Перевірка, що URL правильний і має правильний формат
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.strip('/').split('/')

        # Перевірка на правильну кількість частин (власник/репозиторій)
        if len(path_parts) >= 2:
            repo_branch = path_parts[3]
            return repo_branch
        else:
            raise ValueError("Invalid GitHub URL format")
    else:
        raise ValueError("Not a valid GitHub URL")

# Приклад використання функції
repo_url = "https://github.com/nretrorsum/crypto_dashboard_project/tree/master"
owner = extract_repo_owner(repo_url)
repo_name = extract_repo_name(repo_url)
branch = extract_repo_branch(repo_url)

print(f"Owner: {owner}")
print(f"Repository Name: {repo_name}")
print(f'Repository Branch: {branch}')