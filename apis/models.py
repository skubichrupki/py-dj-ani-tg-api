from django.db import models
from django.utils import timezone

# Create your models here.

class Quotes(models.Model):
    quote_id = models.AutoField(primary_key=True)
    quote_content = models.CharField(default='')
    quote_character_name = models.CharField(default='')
    quote_anime_name = models.CharField(default='')
    created_date = models.DateTimeField(default=timezone.now())
    is_sent = models.IntegerField(default=0)
