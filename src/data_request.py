from httpx import AsyncClient
from config import GITHUB_API_TOKEN
import asyncio

#b89eb169715b2ed32135618eafdebfec0e276b21


async def process_files(self, items, file_paths):
    for item in items:
        if item['type'] == 'blob':
            file_paths.append(item['path'])
        elif item['type'] == 'tree':
            await self.process_directory(item['sha'], file_paths)

class GitHubDataRequest:
    async def get_project_tree(self, token: str, owner: str, repo: str, branch: str):
        url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        }
        async with AsyncClient() as client:
            r = await client.get(url, headers=headers)
            if r.status_code == 200:
                data = r.json()
                # Фільтруємо файли
                files = [item["path"] for item in data.get("tree", []) if item["type"] == "blob"]
                return files
            else:
                print(f"Помилка: {r.status_code} - {r.text}")
                return []

    async def get_repository_data(self, owner, repo, path):
        pass


async def main():
    github = GitHubDataRequest()
    result = await github.get_project_tree(GITHUB_API_TOKEN, 'nretrorsum', 'crypto_dashboard_project', 'master')
    #print(f'project_schema = {project_schema}')
    print(f'result = {result}')

if __name__ == '__main__':
    asyncio.run(main())