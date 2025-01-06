from fastapi import FastAPI
from starlette.responses import FileResponse
import os
from src.test import github_data_request
from src.core_functions import extract_repo_name, extract_repo_owner, extract_repo_branch
from config import BASE_DIR
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.post('/review')
async def create_review(github_repo_url: str):
    owner = extract_repo_owner(github_repo_url)
    repo = extract_repo_name(github_repo_url)
    branch = extract_repo_branch(github_repo_url)

    repo_tree = await github_data_request.get_repository_tree(owner, repo, branch)
    repo_data = await github_data_request.get_repository_data(owner, repo)

    return {'status': '200', 'repo_tree': repo_tree}

@app.get('/get_file')
async def get_file():
    logging.info(f'base dir path:{BASE_DIR}')
    file_path = os.path.join(BASE_DIR, 'code.txt')
    logging.info(f'file_path:{file_path}')
    return FileResponse(file_path)