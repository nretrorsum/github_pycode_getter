import httpx
import logging
from config import OPENAI_API_TOKEN
from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)


async def openai_request(description: str, grade: str):

    with open('code.txt', 'r') as file:
        code = file.read()
        print("File content successfully read.")
    logging.info(f'Grade: {grade}')
    logging.info(f'Description: {description}')
    logging.info(f'Code: {code}')
    logging.info(f'API Token: {OPENAI_API_TOKEN}')
    headers = {
        "Authorization": f"Bearer {OPENAI_API_TOKEN}",
        "Content-Type": "application/json",
    }
    prompt = {
        "model": "gpt-3.5-turbo",  # Змініть на потрібну модель, наприклад, "gpt-3.5-turbo"
        "messages": [
            {"role": "system", "content": "You are a helpful assistant specializing in code reviews."},
            {"role": "user", "content": f"""
            Analyze the following code and provide a structured response based on these criteria:
            1. Key shortcomings.
            2. Comments on this code.
            3. Rate the code from 1 to 10, where 1 is poor and 10 is excellent.
            4. Provide an overall conclusion.

            Context of the project:
            - Project description: {description}
            - Developer's level: {grade}

            Code to analyze:
            {code}
            """}

        ],
        "temperature": 0.3
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=prompt)
        try:
            result = response.json()
            requested_data = result["choices"][0]["message"]["content"]
            if requested_data == None:
                return {'status': response.status_code, 'content': response['message']}

            return requested_data

        except Exception:
            #raise HTTPException(status_code=response.status_code, detail='OpenAI API error')
            pass

