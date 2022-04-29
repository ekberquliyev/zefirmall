from django.contrib import admin
from zefir_mall_app.models import about, company, foodcort, infocenter, navbar, rent
# Register your models here.
admin.site.register(infocenter)
admin.site.register(navbar)
admin.site.register(about)
admin.site.register(rent)
admin.site.register(foodcort)
admin.site.register(company)