from django.contrib import admin

from .models import Account

# Interessante criar uma model para cada account? É possivel
admin.site.register(Account)
