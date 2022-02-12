from django.contrib import admin
from foodwaste.models import CountryLevelWaste,PledgeInfo,SchoolWaste,OrganicImage
# Register your models here.
admin.site.register(CountryLevelWaste)
admin.site.register(PledgeInfo)
admin.site.register(SchoolWaste)
admin.site.register(OrganicImage)
