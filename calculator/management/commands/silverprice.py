from django.core.management.base import BaseCommand
import requests
import json
from datetime import datetime 
import time

from calculator.models import SilverSpot

class Command(BaseCommand):
    def handle(self, *args , **options):
        # 'https://metals-api.com/api/latest?access_key=pm96d3dbaevidtt816jz7610by7qa5cwp737zd0jv93w9323e80qzmumner7&base=XAG&symbols=USD'
        r = requests.get('https://api.metals.live/v1/spot/silver').json()
        price = r[0]['price']
        timest = int(r[0]['timestamp'])
        timest_conv = datetime.fromtimestamp(int(timest)/1000)
        # timest_conv = datetime.fromtimestamp(timest)
        print(f'Cena srebra to {price} USD/Oz, pochodzi z dnia {timest_conv}, a to timestamp {timest} ')

        actual_price = SilverSpot(
            spot = price,
            price_data = timest_conv,
        )
        actual_price.save()
        return