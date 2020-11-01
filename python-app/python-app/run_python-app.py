import requests


print('hello augustoliks !!!')
print('test external dependencies... ')
res = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(f'get fake rest-api:  {res.json()}')
