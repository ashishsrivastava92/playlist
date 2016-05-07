from django.contrib import admin
from greedy.models import Track, Genre

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'genre')

admin.site.register(Track,TrackAdmin)
admin.site.register(Genre,GenreAdmin)