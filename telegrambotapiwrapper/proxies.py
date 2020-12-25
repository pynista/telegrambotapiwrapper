import requests

from telegrambotapiwrapper import Api


def get_public_ip(api: Api) -> str:
    """Get public ip address."""
    return requests.get('https://checkip.amazonaws.com',
                        proxies=api.proxies).text.strip()
