from .. import models
from .animechan_api import AnimechanAPI

class AnimechanManager():

    def __init__(self, url):
        self.url = url

    def get_animechan_api(self):

        url = self.url
        api = AnimechanAPI(url)
        ani_api_result = api.get_random_quote()
        return ani_api_result

    # api request to animechan
    def insert_quote(self, data):
        content = data['content']
        anime_name = data['anime_name']
        character_name = data['character_name']

        # animechan data database handle
        quotes = models.Quotes(quote_content=content, quote_anime_name=anime_name, quote_character_name = character_name)
        quotes.save()

        # text for telegram
        text = f'{content} ~ {character_name} | {anime_name}'
        return text

    # get latest id from quotes table
    def select_latest_quote(self):
        latest_quote = models.Quotes.objects.latest('quote_id')

        return latest_quote