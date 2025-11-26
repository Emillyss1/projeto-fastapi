import requests

headers = {
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3IiwiZXhwIjoxNzYyMjg4NjU4fQ.r3nJwBuRZsY6PZK8VAxZwHUvHHgB2TBCA1X-zy5sHF4"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())
