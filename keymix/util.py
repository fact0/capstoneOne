import requests


def get_user_id(token):
    """Returns the logged in user's Spotify ID"""

    headers = {'Authorization': 'Bearer ' + token}
    resp = requests.get('https://api.spotify.com/v1/me',
                        headers=headers).json()
    return resp['id']


def get_id(input_name, input_type, token):
    """Returns a response with artists or tracks id"""

    headers = {'Authorization': 'Bearer ' + token}
    payload = {
        'q': input_name,
        'type': input_type,
        'limit': 10
    }
    resp = requests.get('https://api.spotify.com/v1/search',
                        params=payload, headers=headers).json()
    return resp


def get_genres(token):
    """Returns a list of Spotify music genres"""

    headers = {'Authorization': 'Bearer ' + token}
    resp = requests.get(
        'https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=headers).json()
    genres = [(genre, genre.capitalize()) for genre in resp['genres']]
    genres[0] = ('', 'Select Genre')
    return genres


def get_keys():
    """Returns a list keys"""

    keys = [('', 'Select a Song Key'), ('1', 'C'), ('2', 'C♯/D♭'), ('3', 'D'), ('4', 'D♯/E♭'), ('5', 'E'),
            ('6', 'F'), ('7', 'F♯/G♭'), ('8', 'G'), ('9', 'G♯/A♭'), ('10', 'A'), ('11', 'A♯/B♭'), ('12', 'B')]
    return keys


def get_modes():
    """Returns a list modes (major or minor key)"""

    keys = [('', 'Select Major or Minor Key'), ('0', 'Minor'), ('1', 'Major')]
    return keys


def create_playlist(user_id, token, playlist_str):
    """Creates an empty Spotify playlist for the logged in Spotify account"""
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    data = '{"name": ' + '"' + playlist_str + '"' + '}'
    
    resp = requests.post(
        f'https://api.spotify.com/v1/users/{user_id}/playlists', headers=headers, data=data).json()
    return resp['id']


def add_songs_to_playlist(playlist_id, track_list, token):
    """Adds tracks to playlist for the logged in Spotify Account"""

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    params = {'uris': track_list}
    resp = requests.post(
        f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers, params=params).json()
    return resp
