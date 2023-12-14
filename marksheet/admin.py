from django.contrib import admin

from marksheet.models import Marksheet
from django.contrib import admin

# Register your models here.
#admin.site.register(Marksheet)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "dob",)
  
admin.site.register(Marksheet, MemberAdmin)