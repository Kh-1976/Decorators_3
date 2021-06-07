import requests
import logging
from datetime import datetime as dt
import os


def decorator_function(fn):

    def foo(*args, **kwargs):
        result = fn(*args) + '!'
        path = kwargs['path']
        logging.basicConfig(filename=os.path.join(path, 'logger.log'), level=logging.INFO)
        logging.info([str(dt.now())[:-7], fn.__name__, *args, result])
        return result
    return foo


lst_heroes = ['Hulk', 'Captain America', 'Thanos']


@decorator_function
def intelligence_max(lst_heroes):
    url = "https://superheroapi.com/api/2619421814940190/search/"
    max_intelligence, hero = 0, ''
    for i in lst_heroes:
        url_hero = url + i
        resp = requests.get(url_hero)
        lst_hero = resp.json()['results']
        if int(lst_hero[0]['powerstats']['intelligence']) > max_intelligence:
            max_intelligence = int(lst_hero[0]['powerstats']['intelligence'])
            hero = i
    return hero


print(intelligence_max(lst_heroes, path='C:\\Logs'))
