from django.contrib import admin
from .models import Post, Equipe, Palestra, Atletica


admin.site.register(Atletica)
admin.site.register(Palestra)
admin.site.register(Equipe)
admin.site.register(Post)
