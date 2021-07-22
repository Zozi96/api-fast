import requests

URL = 'http://127.0.0.1:5000/reviews/list'
HEADERS = {'content-type': 'application/json'}

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print('Petición realizada de forma exitosa')

    print(f'{response.content} \n {response.headers}')

    if response.headers.get('content-type') == 'application/json':
        print(response.json())