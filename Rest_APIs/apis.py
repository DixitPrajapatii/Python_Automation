import requests

ur = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-3-15&to=2024-3-17&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = ur.json()
print(content['articles'])