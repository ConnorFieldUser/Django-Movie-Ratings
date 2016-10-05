from django.contrib import admin
from movie_ratings.models import Item, Rater, Data

# Register your models here.
admin.site.register(Item)
admin.site.register(Rater)
admin.site.register(Data)
