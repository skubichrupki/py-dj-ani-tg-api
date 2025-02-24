import requests

# check the telegram bot api docs
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# res = requests.get(url)
# print(res._content)

class TelegramApi():

    def __init__(self, TOKEN, chat_id, text):
        self.TOKEN = TOKEN
        self.chat_id = chat_id
        self.text = text

    def get_url(self):
        url = f'https://api.telegram.org/bot{self.TOKEN}/sendMessage'
        return url

    def get_params(self):
        params = {
            'chat_id': self.chat_id,
            'text': self.text
        }
        return params

    def send_text(self):
        url = self.get_url()
        params = self.get_params()

        try:
            response = requests.get(url, params=params)
            return response.status_code
        except Exception as e:
            return(str(e))