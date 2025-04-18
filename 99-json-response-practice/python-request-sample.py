<<<<<<< HEAD
import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

# json을 python 타입으로 변환
result = response.json()

print(type(result))
# pprint(result)
# pprint(result[0])
# pprint(result[0].get('title'))
=======
import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

# json을 python 타입으로 변환
result = response.json()

print(type(result))
# pprint(result)
pprint(result[0])
pprint(result[0].get('title'))
>>>>>>> 1bb3fbce50aeea455c64baacf7a4100358d0dd1e
