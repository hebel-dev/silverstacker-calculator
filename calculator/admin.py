from re import split

from requests.api import request
from calculator.models import Coin,SilverSpot
from django.contrib import admin
from decimal import Decimal

admin.register(Coin)
admin.register(SilverSpot)

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):

    list_display = ("name", "coin_weight_in_pure_Ag","last_spot_value","value_to_buy")

    def last_spot_value(self, obj):
        spot = str(SilverSpot.objects.last())
        spot = Decimal(spot)
        return spot
    
    @admin.display()
    def value_to_buy(self, obj):
        silver_spot_data = self.last_spot_value(obj)
        weight_in_silver = obj.coin_weight_in_pure_Ag
        weight_in_silver = Decimal(weight_in_silver)
        to_buy = weight_in_silver * silver_spot_data
        return to_buy 
    
@admin.register(SilverSpot)
class SilverSpotAdmin(admin.ModelAdmin):
    list_display = (
        "spot","price_data"
        )
