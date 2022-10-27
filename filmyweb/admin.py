from django.contrib import admin
from .models import Film

# Register your models here.

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["tytul","opis","rok"] # wybieramy co ma byc widoczne w admin
    #exclude = ["opis"]  #wszystko oprocz opisu
    list_display = ["tytul","imdb_rating","rok"] #jak widac filmy
    list_filter = ("rok",) #dodanie filtru
    search_fields = ("tytul",) #szukajka po tytule