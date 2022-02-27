from django.contrib import admin
from .models import Section
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    fields = ('title','content','parent','user','slug')
admin.site.register(Section, SectionAdmin)