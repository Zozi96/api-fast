import requests

URL = 'http://127.0.0.1:5000/reviews/list'

response = requests.get(URL)

if response.status_code == 200:
    print('Petición realizada de forma exitosa')

    print(response.content)
