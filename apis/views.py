from django.http import JsonResponse
from django.shortcuts import render
from .services.animechan_api import AnimechanAPI
from .services.animechan_manager import AnimechanManager
from .services.telegram_api import TelegramApi
from .services.telegram_manager import TelegramManager
from . import models

# Create your views here.

# /index view
def index(request):

    # database handling
    quotes = models.Quotes.objects.all()
    quotes_count = models.Quotes.objects.count()

    # data
    context = {
        'quotes': quotes,
        'quotes_count': quotes_count
    }

    # rendering
    return render(request=request, template_name='apis/index.html', context=context)

# /animechan view
def animechan():

    url = 'https://animechan.io/api/v1/quotes/random'

    # animechan random quote api and db insert
    ani_manager = AnimechanManager(url=url)

    # api
    ani_api_result = ani_manager.get_animechan_api()
    # db
    ani_insert_result = ani_manager.insert_quote(ani_api_result) # text for tg
    print(ani_insert_result)
    if ani_api_result:
        latest_quote_id = ani_manager.select_latest_quote()

    # send text with telegram api and db update
    tg_manager = TelegramManager(ani_insert_result)

    # api
    tg_api_result = tg_manager.get_telegram_api()
    if tg_api_result == 200:
        # db
        tg_update_result = tg_manager.update_quote(quote_id=latest_quote_id)
    print(tg_update_result)
