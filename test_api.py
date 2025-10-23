import requests

def test_status_code():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
