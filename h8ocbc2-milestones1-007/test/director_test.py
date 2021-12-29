import json
import config

connex_app = config.connex_app
connex_app.add_api('swagger.yml')
connex_app = connex_app.app

client = connex_app.test_client()


def test_director_read_all():
    url = '/api/director'

    response = client.get(url)
    data = json.loads(response.get_data())
    assert isinstance(data, list) is True
    assert response.status_code == 200

def test_post_route__success():
    url = '/api/director'

    mock_request_data = {
        "department": "Directing",
        "gender": 2,
        "name": "Yosianus",
        "uid": 1123
    }
    

    response = client.post(url, data=json.dumps(mock_request_data))
    assert response.status_code == 200
