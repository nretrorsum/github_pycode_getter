# github_pycode_getter
Small web application which get you code from GitHub repo

Use statement:
1) Use command: 
    ```
   git clone https://github.com/nretrorsum/github_pycode_getter.git
   ```
2) Make .env file
3) Add GITHUB_API_TOKEN string and paste your GitHub API token
4) To start app type to cmd:
    ```
    cd ...(directory with project)
    uvicorn src.app:app --reload
   ```

Usage:
Send a POST request to the /review endpoint with the desired GitHub repository URL.
Example input:
```
https://github.com/nretrorsum/github_pycode_getter/tree/master
```
Note: The repository URL must include the branch name, such as /master, /main, etc.

The retrieved code will be saved in a file named code.txt located in the project directory.

