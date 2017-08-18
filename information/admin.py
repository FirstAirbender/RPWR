from django.contrib import admin
from information.models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
class buldingimageInLine(NestedStackedInline):
	model = BuildingImage
	extra = 1


class buildingAdmin(NestedModelAdmin):
	model = Building
	extra = 1
	inlines = [buldingimageInLine]

class InformationAdmin(NestedModelAdmin):
	list_display = ('First_Name', 'Last_Name')


admin.site.register(Information, InformationAdmin)
admin.site.register(Building, buildingAdmin)