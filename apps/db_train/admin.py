from django.contrib import admin

# Зарегистрируйте свои модели в админ панели здесь
from .models import Author

admin.site.register(Author)