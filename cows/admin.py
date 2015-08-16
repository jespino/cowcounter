from django.contrib import admin
from cows.models import Cow, Sell, SentToSlaughterhouse, InExplotationDeath, Expenses, Earnings


class CowAdmin(admin.ModelAdmin):
    list_display = ('crotal_number', 'name', 'sex', 'raze', 'birth_date', 'is_father', 'is_mother', 'is_feeding')
admin.site.register(Cow, CowAdmin)


class SellAdmin(admin.ModelAdmin):
    list_display = ('cow', 'date', 'explotation_code', 'sell_price')
admin.site.register(Sell, SellAdmin)


class InExplotationDeathAdmin(admin.ModelAdmin):
    list_display = ('cow', 'date', 'reason')
admin.site.register(InExplotationDeath, InExplotationDeathAdmin)


class SentToSlaughterhouseAdmin(admin.ModelAdmin):
    list_display = ('cow', 'date', 'weight', 'sell_price')
admin.site.register(SentToSlaughterhouse, SentToSlaughterhouseAdmin)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'type', 'price', 'quantity', 'total')
admin.site.register(Expenses, ExpensesAdmin)


class EarningsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'type', 'price', 'quantity', 'total')
admin.site.register(Earnings, EarningsAdmin)
