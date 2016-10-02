from django.contrib import admin

from baseservice.models import common_user, common_business, common_business_type

admin.site.register(common_user)
admin.site.register(common_business)
admin.site.register(common_business_type)
