import requests

def GetRequest():
    session = requests.Session()

    request = session.get('http://github.com', timeout = 0.05)

    print(request)

    return request