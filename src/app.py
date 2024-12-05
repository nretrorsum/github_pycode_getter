from fastapi import FastAPI
from src.test import github_data_request
from src.core_functions import extract_repo_name, extract_repo_owner, extract_repo_branch
from src.request import openai_request

app = FastAPI()

@app.post('/review')
async def create_review(assignment_description: str, github_repo_url: str, candidate_level: str):
    owner = extract_repo_owner(github_repo_url)
    repo = extract_repo_name(github_repo_url)
    branch = extract_repo_branch(github_repo_url)

    repo_tree = await github_data_request.get_repository_tree(owner, repo, branch)
    repo_data = await github_data_request.get_repository_data(owner, repo)
    review = await openai_request(assignment_description, candidate_level)



    return {'status': '200', 'repo_tree': repo_tree, 'review': review}

