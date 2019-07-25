from django.contrib import admin
from .models import Language, Word, Translation


admin.site.register(Language)
admin.site.register(Word)
admin.site.register(Translation)