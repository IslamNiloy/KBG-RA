from django.contrib import admin
from django.utils.html import format_html
from ckeditor.widgets import CKEditorWidget
from django.db import models
from.models import ContactForm,HomePage,Office,AboutSection,TeamMemberKBG,TeamMemberKBGRA

# Register your models here.

admin.site.register(ContactForm)



class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_background_photo')

    def display_background_photo(self, obj):
        return format_html('<a href="{}" target="_blank"><img src="{}" height="80" /></a>', obj.background_photo.url, obj.background_photo.url)
    display_background_photo.short_description = 'Background Photo'

admin.site.register(HomePage, HomePageAdmin)

   
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_display')
    def image_display(self, obj):
        return format_html('<a href="{}" target="_blank"><img src="{}" height="80" /></a>',obj.image.url,obj.image.url)
    image_display.short_description = 'Image'
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(AboutSection, AboutSectionAdmin)


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('title', 'email','active')
    list_filter = ('active',)
    search_fields = ('title', 'address', 'cellphone', 'email')

admin.site.register(Office, OfficeAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

admin.site.register(TeamMemberKBG, TeamMemberAdmin)


class TeamMemberRAAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

admin.site.register(TeamMemberKBGRA, TeamMemberRAAdmin)


