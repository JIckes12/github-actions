import pytest
from webapp.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    response = client.post('/', json={'num1': 2, 'num2': 23})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 25

    response = client.post('/', json={'num1': 0, 'num2': 0})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 0


def test_subtraction(client):
    response = client.post('/subtraction', json={'num1': 239, 'num2': 5})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 234

def test_division_endpoint(client):
    response = client.post('/division', json={'num1': 18, 'num2': 9})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 2
