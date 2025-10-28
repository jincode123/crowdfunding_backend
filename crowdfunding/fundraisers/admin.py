from django.contrib import admin

from .models import Campaign, Fundraiser, Pledge, Sponsor

admin.site.register(Campaign)
admin.site.register(Fundraiser)
admin.site.register(Pledge)
admin.site.register(Sponsor)
