import requests

api_key = "6932424c3e58424eac577dee26789633"

url = "https://newsapi.org/v2/everything?"\
       "q=tesla&from=2025-01-03&sortBy=publishedAt&"\
       "apiKey=6932424c3e58424eac577dee26789633"

# Make a request
request = requests.get(url)

#Get the dictionary with data
content = request.json()

#  the article title and description
for article in content["articles"]:
    print(content["title"])
    print(content["description"])
