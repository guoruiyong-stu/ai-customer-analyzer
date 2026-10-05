import requests
from config import DEEPSEEK_API_KEY


url = "https://api.deepseek.com/chat/completions"


def analyze_customer(customer):

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }


    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": f"""
分析客户：

公司：
{customer["company"]}

需求：
{customer["need"]}

预算：
{customer["budget"]}

请返回JSON：
{{
"level":"",
"score":0,
"reason":"",
"action":""
}}
"""
            }
        ]
    }


    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=30
    )


    response.raise_for_status()


    result = response.json()

    import json

    answer = result["choices"][0]["message"]["content"]

    answer = answer.replace("```json", "")
    answer = answer.replace("```", "")

    ai_result = json.loads(answer)

    return ai_result

