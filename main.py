import requests

api_key ="77eea1d4f27047bd94f93b27fc8c7e8e"
url="https://newsapi.org/v2/everything?q=tesla&from=2026-08-22&sortBy=publishedAt&apiKey=77eea1d4f27047bd94f93b27fc8c7e8e"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
request = requests.get(url, headers=headers)
content = request.text
print(content)
