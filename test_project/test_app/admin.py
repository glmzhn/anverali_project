from django.contrib import admin
from .models import Executor, Orderer, Experience

admin.site.register(Executor)
admin.site.register(Experience)
admin.site.register(Orderer)
