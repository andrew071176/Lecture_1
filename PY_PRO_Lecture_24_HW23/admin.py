from django.contrib import admin
from .models import About, Who_us, Menu, Specials, Events

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'photo']
    list_editable = ['title', 'desc', 'photo']

@admin.register(Who_us)
class Who_usAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible', 'desc', 'photo']
    list_editable = ['title', 'position', 'is_visible', 'desc', 'photo']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc',
                    'price', 'photo', 'is_special']
    list_editable = ['position', 'is_visible', 'price']

@admin.register(Specials)
class SpecialsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc',
                    'photo', 'is_special']
    list_editable = ['position', 'is_visible']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible', 'desc',
                    'price', 'photo']
    list_editable = ['position', 'is_visible', 'price']
