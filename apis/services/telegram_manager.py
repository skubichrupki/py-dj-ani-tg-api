from telegram_api import TelegramApi


class TelegramManager():

    TOKEN = ''
    chat_id = ''

    def __init__(self, text):
        self.text = text

    def get_telegram_api(self,):
        TOKEN = self.TOKEN
        chat_id = self.chat_id
        text = self.text
        api = TelegramApi(TOKEN=TOKEN, chat_id=chat_id, text=text)
        response = api.send_text()
        return response

    def update_quote(self, quote_id):
            update_result = quote_id.is_sent = 1
            return update_result
        
        # to do: import telegram data from .env