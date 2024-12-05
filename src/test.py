from httpx import AsyncClient, Timeout
import base64
import logging
from core_functions import save_code_in_file, delete_file_content
from config import GITHUB_API_TOKEN
from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)


class GitHubDataRequest:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {GITHUB_API_TOKEN}",
            "Accept": "application/vnd.github+json",
        }
        logging.info(f'Github API token: {GITHUB_API_TOKEN}')

    async def fetch_file_content(self, url):
        """Отримує вміст файлу за його URL."""
        timeout = Timeout(30.0)
        async with AsyncClient(timeout = timeout) as client:
            response = await client.get(url, headers=self.headers)
            logging.info(f"Headers: {self.headers}")
            logging.info(f"Response status: {response.status_code}")
            print(response.json())
            if response.status_code == 200:
                data = response.json()
                if data['type'] == 'file':
                    content = base64.b64decode(data['content']).decode('utf-8')
                    print(f"Content of {data['path']}:")
                    print(content)
                    save_code_in_file(content)
                    logging.info(f"Saved {data['path']}")
                else:
                    raise HTTPException(status_code=response.status_code, detail=f'{data['path']} is not a file')
            else:
               raise HTTPException(status_code=response.status_code, detail=f'Failed to fetch file content from {url}')

    async def traverse_directory(self, url):
        async with AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            logging.info(f"Headers: {self.headers}")
            if response.status_code == 200:
                items = response.json()
                for item in items:
                    if item['type'] == 'file':
                        if not item['name'].endswith(('.pyc', 'jpg', 'jpeg', 'png', 'txt')) :
                            await self.fetch_file_content(item['url'])
                    elif item['type'] == 'dir':
                        await self.traverse_directory(item['url'])
            else:
                raise HTTPException(status_code=response.status_code, detail=f'Failed to fetch directory from {url}')

    async def get_repository_tree(self, owner: str, repo: str, branch: str):
        """Отримує дерево проекту на основі гілки."""
        url = f"{self.base_url}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
        async with AsyncClient() as client:
            r = await client.get(url, headers=self.headers)
            logging.info(f"Headers: {self.headers}")
            if r.status_code == 200:
                data = r.json()
                files = [item["path"] for item in data.get("tree", []) if item["type"] == "blob"]
                return files
            else:
                print(f"Помилка: {r.status_code} - {r.text}")
                return []

    async def get_repository_data(self, owner: str, repo: str, path: str = ''):
        """Отримує дані репозиторію для заданого шляху."""
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
        delete_file_content()
        await self.traverse_directory(url)


github_data_request = GitHubDataRequest()

