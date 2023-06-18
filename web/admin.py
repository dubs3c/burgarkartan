from django.contrib import admin

# Register your models here.
from .models import Teams, Photos, Places, Reviews


admin.site.register(Teams)
admin.site.register(Photos)
admin.site.register(Places)
admin.site.register(Reviews)