import requests

query = input("What type are you intrested today: ")
api = "d0ae85080e8f496b9e99d7326bdee882"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-09-17&sortBy=publishedAt&apiKey={api}"

print(url)

r =  requests.get(url)

data  = r.json()
articles = data['articles']

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n**** **** **** ****\n")
