import os
import requests
from urllib.parse import urlparse

from dotenv import load_dotenv


class BitlyApiKeyMissing(KeyError):
    pass


def remove_scheme(url):
    """Removes http/https prefix in url"""
    parsed_url = urlparse(url)
    return f'{parsed_url.netloc}{parsed_url.path}'


def shorten_link(token, url):
    """Shorten link using bitly API"""
    headers = {
        'Authorization': f'Bearer {token}',
    }
    json_data = {
        'long_url': url,
    }
    api_url = 'https://api-ssl.bitly.com/v4/shorten'

    response = requests.post(api_url, headers=headers, json=json_data)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    """Receives count clicks at shorten link using bitly API"""
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'unit': 'day',
        'units': -1,
    }
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'

    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    """Check is it short link using bitly API"""
    headers = {
        'Authorization': f'Bearer {token}',
    }
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'

    response = requests.get(api_url, headers=headers)
    return response.ok


def main():

    load_dotenv()

    token = os.getenv('BITLY_API_KEY')
    if not token:
        raise BitlyApiKeyMissing('Не указан BITLY API KEY!')

    url = input('Введите ссылку: ')
    no_scheme_url = remove_scheme(url)

    try:
        if is_bitlink(token, no_scheme_url):
            total_clicks = count_clicks(token, no_scheme_url)
            print(f'По вашей ссылке прошли: {total_clicks} раз(а)')
        else:
            bitlink = shorten_link(token, url)
            print('Битлинк:', bitlink)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку')


if __name__ == '__main__':

    main()
