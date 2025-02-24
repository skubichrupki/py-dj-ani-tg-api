import requests

class AnimechanAPI():
    '''class to handle animechan api'''

    # function to create constructors, and pass arguemnts (passed url or default)
    def __init__(self, url):
        self.url = url # assign url from parameter into Class parameter

    def get_random_quote(self):
        '''fetch random anime quote from api'''
        url = self.url

        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            content = json['data']['content']
            anime_name = json['data']['anime']['name']
            character_name = json['data']['character']['name']
            data = {
                'content': content,
                'anime_name' : anime_name,
                'character_name': character_name
            }

            return data
        else:
            return response.status_code