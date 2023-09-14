import requests


# http://data.fixer.io/api/latest?access_key=4df2f384a958fbffd3a12a01bbb06a62
# http://data.fixer.io/api/convert?access_key={API_KEY}&from={val1}&to={val2}&amount={cnt}
# response = requests.get(f'http://data.fixer.io/api/latest?access_key=4df2f384a958fbffd3a12a01bbb06a62')
# res_j = response.json()
# print(res_j['rates'])

url = 'https://api.exchangerate.host/convert?from=USD&to=RUB&amount=10'
response = requests.get(url)
data = response.json()
print(data)

