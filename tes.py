import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=C8F573AQ9Q7LWQAI'
r = requests.get(url)
data = r.json()

print(data)