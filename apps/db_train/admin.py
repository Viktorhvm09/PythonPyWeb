from django.contrib import admin

# Зарегистрируйте свои модели в админ панели здесь
from .models import Author, AuthorProfile, Entry, Tag

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Entry)
admin.site.register(Tag)