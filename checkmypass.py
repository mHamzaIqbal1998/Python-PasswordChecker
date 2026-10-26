import requests

url = 'https://api.pwnedpasswords.com/range/'+'aaf4c'

res= requests.get(url)
print(res)