from django.contrib import admin
# import your models here
from . models import Finch, Feeding, Birdhouse

# Register your models here
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Birdhouse)