import requests


def test_post_authorize():
    payload = {'name': 'Ardmorto'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52355/authorize',
        json=payload,
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    token = data['token']
    username = data['user']
    assert username == 'Ardmorto'
    return token

def test_token_alive():
    response = requests.get(f'http://167.172.172.115:52355/authorize/{test_post_authorize()}')
    assert response.status_code == 200

def test_get_all_memes():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': test_post_authorize()
    }
    response = requests.get(
        'http://167.172.172.115:52355/meme',
        headers=headers
    )
    assert response.status_code == 200

def test_get_meme_by_id():
    test_id = 158
    headers = {
        'Content-Type': 'application/json',
        'Authorization': test_post_authorize()
    }
    response = requests.get(
        f'http://167.172.172.115:52355/meme/{test_id}',
        headers=headers
    )
    assert response.status_code == 200

def test_add_new_meme():
    payload = {
        'text': 'new meme from Ardmorto!',
        'url': 'https://www.graygroupintl.com/hubfs/Gray%20Group%20International/GGI%20-%20Assign%20and%20Sort%20%28WebP%29/Cat%20Memes%20The%20Viral%20Phenomenon.webp',
        'tags': ['cat', 'it'],
        'info': {
            'type': ['picture', 'webp format', 'ai generated'],
            'rating': 9
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': test_post_authorize()
    }
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=payload,
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    id = data['id']
    return id

def test_change_meme():
    payload = {
        'id': 987666,
        'text': 'meme from Ardmorto with changes',
        'url': 'https://www.graygroupintl.com/hubfs/Gray%20Group%20International/GGI%20-%20Assign%20and%20Sort%20%28WebP%29/Cat%20Memes%20The%20Viral%20Phenomenon.webp',
        'tags': ['cat', 'it'],
        'info': {
            'type': ['picture', 'webp format', 'ai generated'],
            'rating': 9
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': test_post_authorize()
    }
    response = requests.put(
        f'http://167.172.172.115:52355/meme/{test_add_new_meme()}',
        json=payload,
        headers=headers
    )

def test_delete_meme():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': test_post_authorize()
    }
    response = requests.delete(f'http://167.172.172.115:52355/meme/{test_add_new_meme()}', headers=headers)