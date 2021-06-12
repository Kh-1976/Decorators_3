import requests
import logging
from datetime import datetime as dt
import os


def parametrized_decor(parameter):
    def decorator_function(fn):
        def foo(*args):
            logging.basicConfig(filename=os.path.join(parameter, 'logger.log'), level=logging.INFO)
            result = fn(*args) + '!'
            logging.info([str(dt.now())[:-7], fn.__name__, *args, result])
            return result
        return foo
    return decorator_function


lst_heroes = ['Hulk', 'Captain America', 'Thanos']


@parametrized_decor(parameter='C:\\Logs')
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


print(intelligence_max(lst_heroes))
