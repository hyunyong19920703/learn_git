import pytest

from hello import app


@pytest.fixture
def client():
    return app.test_client()

def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()

def test_home(client):        
    
    # first response
    status_code, body, data = do_get(client, '/')    
    assert status_code == 200
    assert '"text":"Hello, World!"' in body  
    old_count = data['count']
    
    # second response
    status_code, body, data = do_get(client, '/')
    assert status_code == 200   
    new_count = data['count']
    assert new_count == old_count + 1
    
def test_abuse(client):
    
    # first response
    status_code, body, data = do_get(client, '/')
    old_count = data['count']
    
    assert status_code == 200
    
    status_code, _, _ = do_get(client, '/abuse')
    
    assert status_code == 200
    
    status_code, body, data = do_get(client, '/')
    new_count = data['count']
    
    assert status_code == 200
    assert new_count == old_count + 100 + 1