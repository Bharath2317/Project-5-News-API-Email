import requests
from send_email import send_email

topic = "tesla"
api_key = "6932424c3e58424eac577dee26789633"
url = "https://newsapi.org/v2/everything?"\
       f"q={topic}" \
        "&""from=2025-01-04&sortBy=publishedAt&"\
       "apiKey=6932424c3e58424eac577dee26789633"\
        "&language=en"

# Make a request
request = requests.get(url)

#Get the dictionary with data
content = request.json()

#  the article title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" \
               + "\n"+ body + article["title"] + "\n" \
               +article["description"] \
               +"\n"+article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)


