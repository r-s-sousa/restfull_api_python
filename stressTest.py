import requests

def getBaseUrl():
    baseUrl = 'http://localhost:5000'
    return baseUrl

def getBooks(cont, endpoint = '/books'):
    response = requests.get(getBaseUrl() + endpoint)
    print(f"get books: {cont} º : {response.status_code}")

def postBooks(cont, endpoint = '/books'):
    response = requests.post(getBaseUrl() + endpoint, json={ "id": cont, "title": "Python Programming", "author": "John Doe" })
    print(f"post books: {cont} º : {response.status_code}")

def main():
    cont = 10000
    for i in range(cont):
        getBooks(i+1)
        postBooks(i+1)

main();