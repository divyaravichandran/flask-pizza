from django.contrib import admin

from .models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs, Pasta, Salad, Dinner_Platter


admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Dinner_Platter)
